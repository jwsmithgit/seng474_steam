import sys
import json
import urllib.request
import time

print( "usage python .\\6removeoldscrape.py data.json outfile.json" )

url_start = "http://store.steampowered.com/api/appdetails?appids="

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

for item in list(data):
    appid = data[item]["appid"]
    print(appid)

    time.sleep(1)
    request = urllib.request.Request(url_start + appid)
    with urllib.request.urlopen(request) as response:
        url_data = response.read().decode("utf-8")

    while( url_data == "null" or url_data == "" ):
        time.sleep(60)
        request = urllib.request.Request(url_start + appid)
        with urllib.request.urlopen(request) as response:
            url_data = response.read().decode("utf-8")
        print( "retrying" )

    colon = url_data.find(':')
    url_data = url_data[colon+1:-1]

    json_data = json.loads(url_data)
    if (json_data["success"] == False) :
        print("removed")
        data.pop(item)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
