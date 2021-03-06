import sys
import json
import urllib.request
import time

print( "usage python .\\4scrapenew.py newdata.txt outfile.json" )

url_start = "http://store.steampowered.com/api/appdetails?appids="

missing_data = {}

f = open(sys.argv[1], 'r')
for line in f:
    appid = line.strip()
    print(appid)

    time.sleep(1)
    request = urllib.request.Request(url_start + appid)
    with urllib.request.urlopen(request) as response:
        url_data = response.read().decode("utf-8")

    while( True ):#url_data == "null" or url_data == "" ):
        time.sleep(60)
        request = urllib.request.Request(url_start + appid)
        with urllib.request.urlopen(request) as response:
            url_data = response.read().decode("utf-8")
        print( "retrying" )

    colon = url_data.find(':')
    url_data = url_data[colon+1:-1]

    json_data = json.loads(url_data)
    if (json_data["success"] == False) :
        print( "failed on " + appid )
        continue

    missing_data[appid] = json_data["data"]

with open(sys.argv[2], 'w') as outfile:
    json.dump(missing_data, outfile, separators=(',', ':'))
