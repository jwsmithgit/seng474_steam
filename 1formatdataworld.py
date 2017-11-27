import json
import sys

print( "usage python ./1formatdataworld.py dataworld.json outfile.json" )

f = open(sys.argv[1], 'r')

jsf = '{'
for line in f:
    entry_json = json.loads(line)
    if 'data' not in entry_json:
        continue
    print(entry_json['query_appid'])
    jsf += '"' + str(entry_json['query_appid']) + '": ' + json.dumps(entry_json['data']) + ','

jsf = jsf[:-1] + '}'
jsf = json.loads(jsf)

with open(sys.argv[2], 'w') as outfile:
    json.dump(jsf, outfile, separators=(',', ':'))
