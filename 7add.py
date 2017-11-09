import json
import sys

print( "usage python ./7add.py data1.json data2.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data1 = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    data2 = json.load(json_data)

final = {}
for kid in data1:
    final[kid] = data1[kid]

for kid in data2:
    final[kid] = data2[kid]

with open(sys.argv[3], 'w') as outfile:
    json.dump(final, outfile)
