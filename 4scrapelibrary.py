import urllib.request
import json
import sys

print( "usage python ./4scrapelibrary.py userid outfile.json" )

url_start = "http://steamcommunity.com/id/"
url_end = "/games/?tab=all"
url_id = sys.argv[1]

request = urllib.request.Request(url_start + url_id + url_end)

data = ""
with urllib.request.urlopen(request) as response:
   data = response.read().decode("utf-8")

i = data.find("[{\"")
data = data[i:]
i = data.find(";")
data = data[:i]

raw_data = json.loads(data)
final_data = {}
for k in raw_data:
    app_k = k['appid']
    final_data[app_k] = k

with open(sys.argv[2], 'w') as outfile:
    json.dump(final_data, outfile)
