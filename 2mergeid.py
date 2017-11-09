import json
import sys

print( "usage python ./2mergeid.py data1.json data2.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    ss_json = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    dw_json = json.load(json_data)

for kid in ss_json:
    if kid in dw_json:
        for dkey in ss_json[kid]:
            if dkey not in dw_json[kid]:
                dw_json[kid][dkey] = ss_json[kid][dkey]

with open(sys.argv[3], 'w') as outfile:
    json.dump(dw_json, outfile)
