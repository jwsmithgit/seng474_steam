import json
import sys

print( "usage python ./finalformat.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

for instance in data:
    if "success" in data[instance]:
        data[instance].pop("success")
    if "data" in data[instance]:
        for k in data[instance]["data"]:
            data[instance][k] = data[instance]["data"][k]
        data[instance].pop("data")

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile)
