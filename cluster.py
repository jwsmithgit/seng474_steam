import json
import sys
import scipy.cluster.vq as cluster
import matplotlib.pyplot as plt

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

whitened = cluster.whiten( train )
codebook, labels = cluster.kmeans2( train, int(len(data)/20) )

print( labels )
print( len(labels))
print( len(data))
plt.scatter(whitened[:, 0], whitened[:, 1])
plt.scatter(codebook[:, 0], codebook[:, 1], c='r')
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


liblist = list(library)
appid = liblist[2]

appindex = train_id.index(appid)
applabel = labels[appindex]
groupindex = group_id.index(applabel)
groupapp = group[groupindex]
print( appid)
print( groupapp )
