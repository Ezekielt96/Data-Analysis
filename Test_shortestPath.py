import random
import sys

adjacencyGraph = {}
distance = {}
for i in range (0, 20):
    a = random.sample(range(0,20),1)
    tmpList = random.sample(range(0,20),a[0])
    neighborList = []
    for j in tmpList :
        if j != i:
            neighborList.append(j)
        adjacencyGraph[i] = neighborList
        distance[i] = sys.maxsize
print (adjacencyGraph)
            
