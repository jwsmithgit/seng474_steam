import json
import sys
import scipy.cluster.hierarchy as cluster
import pickle

print( "usage python .\\8cluster.py data.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

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
clusterTree = cluster.linkage(Xtrain, 'ward')

#notice that the cluster return is never used directly to demo pickle functionality
#we still need to embed any values we want to use past this point into clusterTree, or write out other objects
with open('cluster.bin', 'wb') as writefile:
    pickle.dump(clusterTree, writefile, protocol=2)

with open('appids.bin', 'wb') as writefile:
    pickle.dump(Xappid, writefile, protocol=2)
