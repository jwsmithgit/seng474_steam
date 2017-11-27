import sys
import json

print( "usage python .\\removebad.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

for item in list(data):
    if data[item]["userscore"] < 50 :
        data.pop(item)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
