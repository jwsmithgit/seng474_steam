import sys
import json
import urllib2
import pickle
import random

url_start = "http://steamcommunity.com/id/"
url_end = "/games/?tab=all"
url_id = sys.argv[1]

request = urllib2.Request(url_start + url_id + url_end)
response = urllib2.urlopen(request)
url_data = response.read().decode("utf-8")

i = url_data.find("[{\"")
url_data = url_data[i:]
i = url_data.find(";")
url_data = url_data[:i]

json_data = json.loads(url_data)
library = {}
for k in json_data:
    app_k = k['appid']
    library[app_k] = k

Z = pickle.load(open('cluster.bin', 'rb'))
Zappids = pickle.load(open('appids.bin', 'rb'))

recommendations = {}
for appid in list(library):
    if str(appid) not in Zappids:
        #print("something went wrong for " + str(appid))
        continue
    appindex = Zappids.index(str(appid))

    leaf = appindex # starting index
    leafs = [] # all leafs in clustering
    size = 3 # how many similar games
    node = 0 # iterable, index of end cluster
    n = len(Zappids)
    while len(leafs) < size:
        #find next cluster with of size m from leaf
        while(1):
            if Z[node][0] == leaf or Z[node][1] == leaf:
                if Z[node][3] < size+1:
                    leaf = node+n
                else:
                    break
            else:
                node += 1
        #node is now the cluster id in the linkage matrix

        #find leaf instances from cluster in linkage matrix
        nodes = [node] # intermittent nodes BFS
        while len(nodes) > 0:
            left = int( Z[nodes[0]][0] )
            right = int( Z[nodes[0]][1] )
            if left < n:
                leafs.append(left)
            else:
                nodes.append(left-n)
            if right < n:
                leafs.append(right)
            else:
                nodes.append(right-n)
            nodes.pop(0)

        #remove leafs from that are in library
        leafs = [x for x in leafs if not Zappids[x] in library]

        if len(leafs) < size:
            leaf = node+n
            leafs = []

    #convert leaf ids to app appids
    for leaf in leafs:
        sid = Zappids[leaf]
        if sid in recommendations:
            recommendations[sid] += 1
        else:
            recommendations[sid] = 1

#not a smart list right now, just 5 games for each list in user library
#for appid in list(recommendations):
##        recommendations.pop(appid)
recommendationlist = []
for k in recommendations:
    recommendationlist.append( (k, recommendations[k]) )
recommendationlist.sort(key=lambda app: app[1], reverse=True)

total_count = 0
for i,v in enumerate( recommendationlist ):
    total_count += v[1]

random.seed()
choice_list = []
while len(choice_list) < 10:
    random_choice = random.randint(0, total_count)
    for i,v in enumerate( recommendationlist ):
        random_choice -= v[1]
        if random_choice < 0 and recommendationlist[i][0] not in choice_list:
            choice_list.append( recommendationlist[i][0] )
            break

#list recommender
print(list(choice_list[:10]))
#single game recommender
#print(choice_list[0])
