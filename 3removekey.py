import json
import sys

print( "usage python ./3removekey.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

key = input("remove? ")
while( key ):
    for kid in data:
        if key in data[kid]:
            del data[kid][key]

    key = input("remove?")

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile)
