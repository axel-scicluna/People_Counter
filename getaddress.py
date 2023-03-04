from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json


def getAddress(yoururl):

    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=caps)
    driver.get(yoururl)

    #finds webcam and clicks it so network traffic can commence
    driver.find_element(by="id",value="webcam").click()
    time.sleep(5)
    #time.sleep(5) # wait for all the data to arrive. 
    logs = driver.get_log('performance')
   
    with open("network_log.json", "w", encoding="utf-8") as f:
        f.write("[")

    # Iterates every logs and parses it using JSON
        for log in logs:
            network_log = json.loads(log["message"])["message"]
            
            # Checks if the current 'method' key has any
            # Network related value.
            if("Network.response" in network_log["method"]
                or "Network.request" in network_log["method"]
                or "Network.webSocket" in network_log["method"]):
            
                # Writes the network log to a JSON file by
                # converting the dictionary to a JSON string
                # using json.dumps().
                f.write(json.dumps(network_log)+",")
        f.write("{}]")
    
    print("Quitting Selenium WebDriver")
    driver.quit()

    # Read the JSON File and parse it using
        # json.loads() to find the urls containing images.
    json_file_path = "network_log.json"
    with open(json_file_path, "r", encoding="utf-8") as f:
            logs = json.loads(f.read())
    
        # Iterate the logs
    for log in logs:
    
            # Except block will be accessed if any of the
            # following keys are missing.
            try:
                # URL is present inside the following keys
                url = log["params"]["request"]["url"]

                
                # Checks if text below exists in the network requests url section of the logs
                if url[0:34] == "https://hd-auth.skylinewebcams.com":
                     break
            except Exception as e:
                pass

    return url


