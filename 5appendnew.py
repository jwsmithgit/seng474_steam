import sys
import json

print( "usage python .\\5appendnew.py old_data.json new_data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    old_data = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    new_data = json.load(json_data)

for item in new_data:
    old_data[item] = new_data[item]

with open(sys.argv[3], 'w') as outfile:
    json.dump(old_data, outfile, separators=(',', ':'))
