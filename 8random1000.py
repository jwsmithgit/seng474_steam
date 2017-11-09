import json
import random
import math
import sys

print( "usage python ./8random1000.py finaldata.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    fjson = json.load(json_data)

new = {}
for i in range(1000):
    appid = random.choice(list(fjson.keys()))
    new[appid] = fjson[appid]

with open(sys.argv[2], 'w') as outfile:
    json.dump(new, outfile)
