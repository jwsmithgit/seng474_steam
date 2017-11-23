import json
import sys
import scipy.cluster.vq as cluster
import scipy.cluster.hierarchy as hier
import matplotlib.pyplot as plt
import sklearn.cluster as cluster2
import itertools
import numpy as np

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
    library = json.load(json_data)

train_id = []
train = []

features = []

#find all tags
for entry in data:
    for tag in data[entry]["tags"]:
        if tag not in features:
            features.append(tag)

for entry in data:
    tags = data[entry]["tags"]
    entry_features = []
    for feature in features:
        if feature in tags:
            entry_features.append(1.)#tags[feature]+0.)
        else:
            entry_features.append(0.)

    train_id.append( entry )
    train.append( entry_features )

#whitened = cluster.whiten( train )
#codebook, labels = cluster.kmeans2( train, int(len(data)/20) )

print('clustering')
'''model = cluster2.AgglomerativeClustering()
model.fit(train)
ii = itertools.count(train.shape[0])
[{'node_id': next(ii), 'left': x[0], 'right':x[1]} for x in model.children_]
'''

Z = hier.linkage(train, 'ward')
np.set_printoptions(formatter={'float_kind':'{:f}'.format})
print(Z)
print( len(train ))
print( len(Z ))




'''print( labels )
print( len(labels))
print( len(data))
#plt.scatter(whitened[:, 0], whitened[:, 1])
#plt.scatter(codebook[:, 0], codebook[:, 1], c='r')
#plt.show()

#inverse labels
group_id = []
group = []

for label in labels:
    if label not in group_id:
        group_id.append(label)
        group.append([])

print( group_id)
print( group )
print( len(group_id))

for i,label in enumerate(labels):
    group[group_id.index(label)].append( train_id[i] )

print( group)
'''

liblist = list(library)
appid = liblist[1]
appindex = train_id.index(appid)

print(appindex)
for merge in Z:
    if appindex in merge:
        print(merge)
        if appindex == merge[0]:
            print( train_id[int(merge[1])] )
        else:
            print( train_id[int(merge[0])] )


'''model.children_(appindex)
'''


'''appindex = train_id.index(appid)
applabel = labels[appindex]
groupindex = group_id.index(applabel)
groupapp = group[groupindex]
print( appid)
print( groupapp )
'''
