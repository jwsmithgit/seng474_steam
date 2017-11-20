import json
import sys

print( "usage python ./deletenotag.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

for entry in list(data):
    if "tags" not in data[entry] or len(data[entry]["tags"]) == 0:
        data.pop(entry)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile)
