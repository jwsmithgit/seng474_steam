import sys
import json

print( "usage python .\\6removekeymanual.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

keys = []
for item in data:
    for key in data[item]:
        if key not in keys:
            keys.append( key )
print( keys )

key = 1
while( key ):
    key = input("")
    if key == "":
        break

    for item in data:
        if key in data[item]:
            data[item].pop(key)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
