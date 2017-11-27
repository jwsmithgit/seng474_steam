import json
import sys

print( "usage python ./removebad.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

for entry in list(data):
    if "userscore" not in data[entry]:
        print( data[entry] )
        print(data[entry]["appid"])
    if data[entry]["userscore"] < 50 :
        data.pop(entry)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
