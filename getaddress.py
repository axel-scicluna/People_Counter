from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import re
yoururl = "https://www.skylinewebcams.com/en/webcam/malta/malta/valletta/valletta-republic-street.html"
wantToFind = "https://hd-auth.skylinewebcams.com/live."

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(desired_capabilities=caps)

driver.get(yoururl)

time.sleep(5) # wait for all the data to arrive. 
perf = driver.get_log('performance')
for i in perf:
    input = str(i)
    result = re.search(wantToFind,input)
    print(result)
#

        #https://hd-auth.skylinewebcams.com/live.

#site_json=json.loads(perf)
#print(site_json)
#printing for entrezgene, do the same for name and symbol
#print([d.get('entrezgene') for d in perf['hits'] if d.get('entrezgene')])

#print(perf)