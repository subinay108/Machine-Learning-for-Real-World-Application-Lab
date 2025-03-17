import random
import math
import numpy as np
import matplotlib.pyplot as plt

random.seed(0)

def generateRandomDataPoints(n, a, b):
    datapoints = []
    for i in range(n):
        x = a + random.random() * (b - a)
        y = a + random.random() * (b - a)
        datapoints.append(np.array((x, y)))

    return datapoints

def euclidean_distance(X, Y):
    s = 0
    for i, j in zip(X, Y):
        s += (i - j) ** 2
    return math.sqrt(s)

def k_means_clustering(datapoints, k = 3, epoch = 10):
    # generate k random centre of clusters
    clusters = []
    for i in range(k):
        centroid = random.choice(datapoints)
        clusters.append(centroid)

    while epoch:
        # assign cluster to each data points
        clusterwise_data = []
        for i in range(len(clusters)):
            clusterwise_data.append([])

        for i in range(len(datapoints)):
            near_dist = euclidean_distance(datapoints[i], clusters[0])
            clusterno = 0
            for j in range(1, len(clusters)):
                dist = euclidean_distance(datapoints[i], clusters[j])
                if near_dist > dist:
                    near_dist = dist
                    clusterno = j
            clusterwise_data[clusterno].append(datapoints[i])
        
        # calculate the mean of datapoints in each cluster
        means_of_clusters = []
        for clusterno in range(len(clusterwise_data)):
            n = 0
            s = np.array([0.0] * len(clusterwise_data[0][0]))
            for datapoint in clusterwise_data[clusterno]:
                s += datapoint
                n += 1
            if n:
                means_of_clusters.append(s / n)
            else:
                means_of_clusters.append([0, 0])

        # adjust centroids closure to the mean
        for i in range(len(clusters)):
            clusters[i] += 1 * (means_of_clusters[i] - clusters[i])

        epoch -= 1

    return clusterwise_data, clusters
        

datapoints = generateRandomDataPoints(300, 0, 100)

clusterwise_data, clusters = k_means_clustering(datapoints, k = 3)

# Plot data points after clustering
X = []
Y = []
c = []
for clusterno in range(len(clusterwise_data)):
    color = random.random()
    for x, y in clusterwise_data[clusterno]:
        X.append(x)
        Y.append(y)
        c.append(color)

plt.scatter(X, Y, c=c)

X = []
Y = []
for x, y in clusters:
    X.append(x)
    Y.append(y)

print(X)
print(Y)
plt.scatter(X, Y, s=150, c='red', marker='*')

plt.show()