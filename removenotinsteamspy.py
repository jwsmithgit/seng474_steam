import json
import sys

print( "usage python ./removenotinsteamspy.py data.json steamspy.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    steamspy = json.load(json_data)

for entry in list(data):
    if entry not in steamspy:
        data.pop(entry)

with open(sys.argv[3], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
