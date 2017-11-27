import json
import sys

print( "usage python ./6removekey.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

keys = []
for kid in data:
    for key in data[kid]:
        if key not in keys:
            keys.append( key )
print( keys )

key = 1
while( key ):
    key = input("remove? ")
    if key == "":
        break

    for kid in data:
        if key in data[kid]:
            data[kid].pop(key)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
