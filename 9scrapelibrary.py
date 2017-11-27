import sys
import json
import urllib.request

print( "usage python .\\9scrapelibrary.py userid outfile.json" )

url_start = "http://steamcommunity.com/id/"
url_end = "/games/?tab=all"
url_id = sys.argv[1]

request = urllib.request.Request(url_start + url_id + url_end)
with urllib.request.urlopen(request) as response:
    url_data = response.read().decode("utf-8")

i = url_data.find("[{\"")
url_data = url_data[i:]
i = url_data.find(";")
url_data = url_data[:i]

json_data = json.loads(url_data)
format_data = {}
for k in json_data:
    app_k = k['appid']
    format_data[app_k] = k

with open(sys.argv[2], 'w') as outfile:
    json.dump(format_data, outfile, separators=(',', ':'))
