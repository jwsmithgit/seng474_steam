import json
import sys

print( "usage python ./5missingdata.py finaldata.json newdata.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    ss_json = json.load(json_data)

missing = ""
for k in ss_json:
    if k not in data:
        missing += str(k) + '\n'

fout = open(sys.argv[3], 'w')
fout.write(missing)
