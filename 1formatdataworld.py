import sys
import json

print( "usage python .\\1formatdataworld.py dataworld.json outfile.json" )

f = open(sys.argv[1], 'r')

formatted_json = '{'
for line in f:
    line_json = json.loads(line)
    if 'data' not in line_json:
        continue
    print(line_json['query_appid'])
    formatted_json += '"' + str(line_json['query_appid']) + '": ' + json.dumps(line_json['data']) + ','

formatted_json = formatted_json[:-1] + '}'
formatted_json = json.loads(formatted_json)

with open(sys.argv[2], 'w') as outfile:
    json.dump(formatted_json, outfile, separators=(',', ':'))
