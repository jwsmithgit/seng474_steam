import sys
import json
import random
import math

print( "usage python .\\9random1000.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

random_1000 = {}
for i in range(1000):
    appid = random.choice(list(data.keys()))
    random_1000[appid] = data[appid]

with open(sys.argv[2], 'w') as outfile:
    json.dump(random_1000, outfile, separators=(',', ':'))
