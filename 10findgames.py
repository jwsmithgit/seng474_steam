import sys
import json
import pickle

with open(sys.argv[1], 'r') as json_data:
    library = json.load(json_data)

with open('cluster.bin', 'rb') as readfile:
    Z = pickle.load(readfile)

with open('appids.bin', 'rb') as readfile:
    Zappids = pickle.load(readfile)

print(library)

recommendationlist = []

for appid in list(library):
    try:
        appindex = Zappids.index(appid)

        #find a cluster with of size m from leaf
        leaf = appindex # starting index
        size = 5 # size of cluster you want
        node = 0 # iterable, index of end cluster
        n = len(Zappids)
        while(1):
            if Z[node][0] == leaf or Z[node][1] == leaf:
                if Z[node][3] < size:
                    leaf = node+n
                else:
                    break
            else:
                node += 1
        #node is now the cluster id in the linkage matrix

        #find leaf instances from cluster in linkage matrix
        node = node # starting cluster
        nodes = [node] # intermittent nodes BFS
        leafs = [] # all leafs in clustering
        n = len(Zappids)

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

        #convert leaf ids to app appids
        similar_appids = []
        for leaf in leafs:
            similar_appids.append( Zappids[leaf] )

        for sid in similar_appids:
            #list recommender
            recommendationlist.append(sid)
            '''
            #single game recommender
            if sid in recommendationlist:
                recommendationlist[sid] += 1
            else:
                recommendationlist[sid] = 0
            '''
    except:
        print("something went wrong for " + str(appid))

#not a smart list right now, just 5 games for each list in user library
#list recommender
for i,appid in enumerate(recommendationlist):
    if appid in library:
        recommendationlist.pop(i)
print(recommendationlist)

'''
#single game recommender
for key in list(recommendationlist):
    if key in library:
        recommendationlist.pop(key)
max_id = max(recommendationlist, key=recommendationlist.get)
print(max_id)
'''
