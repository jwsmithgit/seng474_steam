import requests
from bs4 import BeautifulSoup
import json
import time
import sys

print( "usage python ./6scrapemissing.py missing.txt outfile.json" )

url_start = "http://store.steampowered.com/api/appdetails?appids="
url_end = "/?cc=us"

missing_data = {}

f = open(sys.argv[1], 'r')
for line in f:
    app_id = line.strip()
    print(app_id)

    time.sleep(1)
    result = requests.get(url_start + app_id)# + url_end, cookies=cookies)
    string_data = result.content.decode("utf-8")
    print( string_data )

    while( string_data == "null" or string_data == "" ):
        time.sleep(60)
        result = requests.get(url_start + app_id)# + url_end, cookies=cookies)
        string_data = result.content.decode("utf-8")
        print( string_data )

    colon = string_data.find(':')
    string_data = string_data[colon+1:-1]

    json_data = json.loads(string_data)
    if (json_data["success"] == "failure") :
        continue

    missing_data[app_id] = json_data

with open(sys.argv[2], 'w') as outfile:
    json.dump(missing_data, outfile)
