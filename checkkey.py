import json
import sys

print( "usage python ./checkkey.py data.json" )

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
    key = input("check?")

    for kid in data:
        if key not in data[kid]:
            print(kid + ": " + key)
