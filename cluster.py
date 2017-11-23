import json
import sys
import scipy.cluster.hierarchy as cluster
import matplotlib.pyplot as plt

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    library = json.load(json_data)

Xappid = []
Xtrain = []

categories = []
genres = []
tags = []

features = []

#find all feature names for feature vectors
for instance in data:
    if "categories" in data[instance]:
        for category in data[instance]["categories"]:
            if category["description"] not in categories:
                categories.append(category["description"])

    if "genres" in data[instance]:
        for genre in data[instance]["genres"]:
            if genre["description"] not in genres:
                genres.append(genre["description"])

    for tag in data[instance]["tags"]:
        if tag not in tags:
            tags.append(tag)

#print( categories )
#print( genres )
#print( tags )

#find features in instances
for instance in data:
    instance_features = []

    for category in categories:
        feature = 0.
        if "categories" in data[instance]:
            for ic in data[instance]["categories"]:
                if category == ic["description"]:
                    feature = 1.
        instance_features.append(feature)#tags[feature]+0.)

    for genre in genres:
        feature = 0.
        if "genres" in data[instance]:
            for ig in data[instance]["genres"]:
                if genre == ig["description"]:
                    feature = 1.
        instance_features.append(feature)#tags[feature]+0.)

    for tag in tags:
        if tag in data[instance]["tags"]:
            instance_features.append(1.)#tags[feature]+0.)
        else:
            instance_features.append(0.)

    Xappid.append( instance )
    Xtrain.append( instance_features )

print('clustering')
Z = cluster.linkage(Xtrain, 'ward')

print( len(Xtrain ))
print( len(Z ))

liblist = list(library)
libappid = liblist[2]
libappindex = Xappid.index(libappid)

#find a cluster with of size m from leaf
leaf = libappindex # starting index
size = 5 # size of cluster you want
node = 0 # iterable, index of end cluster
n = len(Xtrain)
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
n = len(Xtrain)

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
appids = []
for leaf in leafs:
    appids.append( Xappid[leaf] )

print(appids)
