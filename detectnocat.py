import json
import sys

print( "usage python ./deletenotag.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

for entry in list(data):
    if "categories" not in data[entry]:
        print( entry )
        #data.pop(entry)


#with open(sys.argv[2], 'w') as outfile:
#    json.dump(data, outfile)
