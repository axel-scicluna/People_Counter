import json
from datetime import datetime

#json.dumps(['date',{datetime.now().strftime("%Y-%m-%d %H:%M:%S")},'Count',{str(2)}])


data = {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
}

with open("data_file.json", "a") as write_file:
    json.dump(data, write_file)