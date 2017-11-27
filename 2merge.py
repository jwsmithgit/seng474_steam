import sys
import json

print( "usage python .\\2merge.py to_data.json from_data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    to_data = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    from_data = json.load(json_data)

for item in from_data:
    if item in to_data:
        for value in from_data[item]:
            to_data[item][value] = from_data[item][value]

with open(sys.argv[3], 'w') as outfile:
    json.dump(to_data, outfile, separators=(',', ':'))
