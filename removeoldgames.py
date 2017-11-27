import requests
from bs4 import BeautifulSoup
import json
import time
import sys

print( "usage python ./6scrapemissing.py data.json outfile.json" )

url_start = "http://store.steampowered.com/api/appdetails?appids="
url_end = "/?cc=us"

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

for entry in list(data):
    app_id = data[entry]["appid"]
    print(app_id)

    #time.sleep(1)
    result = requests.get(url_start + str(app_id))
    string_data = result.content.decode("utf-8")
    #print( string_data )

    while( string_data == "null" or string_data == "" ):
        time.sleep(10)
        result = requests.get(url_start + str(app_id))
        string_data = result.content.decode("utf-8")
        #print( "retrying" )

    colon = string_data.find(':')
    string_data = string_data[colon+1:-1]

    json_data = json.loads(string_data)
    if (json_data["success"] == False) :
        print("removed")
        data.pop(entry)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
