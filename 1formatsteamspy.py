import sys
import json

print( "usage python .\\1formatsteamspy.py steamspy.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

for item in list(data):
    if "tags" not in data[item] or len(data[item]["tags"]) == 0:
        data.pop(item)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
