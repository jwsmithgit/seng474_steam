import json
import sys

print( "usage python ./2merge.py fromdata.json todata.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    fromdata = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    todata = json.load(json_data)

for kid in fromdata:
    if kid in todata:
        for kfield in fromdata[kid]:
            todata[kid][kfield] = fromdata[kid][kfield]

with open(sys.argv[3], 'w') as outfile:
    json.dump(todata, outfile, separators=(',', ':'))
