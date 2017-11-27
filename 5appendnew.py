import json
import sys

print( "usage python ./5appendnew.py data1.json data2.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data1 = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    data2 = json.load(json_data)

final = data1
for kid in data2:
    final[kid] = data2[kid]

with open(sys.argv[3], 'w') as outfile:
    json.dump(final, outfile, separators=(',', ':'))
