import sys
import json

print( "usage python .\\3newdata.py olddata.json newdata.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    old_data = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    new_data = json.load(json_data)

missing = ""
for k in new_data:
    if k not in old_data:
        missing += str(k) + '\n'

fout = open(sys.argv[3], 'w')
fout.write(missing)
