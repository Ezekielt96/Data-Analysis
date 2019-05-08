import random
import sys

# Randomly pick a number between 1 and 20


adjacencyGraph = {}
distance = {}
# R
for i in range(0,20) :
	# For each node create a random range of neighbors
	a = random.sample(range(2,5),1)
	tmpList = random.sample(range(0,20),a[0]) 
	neighborList = []
	for j in tmpList :
		if j != i :
			neighborList.append(j)
	adjacencyGraph[i] = neighborList
	distance[i] = sys.maxsize

print(adjacencyGraph)


headNode = random.sample(range(0,20),1)
S = []
S.append(headNode[0])
V = random.sample(range(0,20),20)

V.remove(headNode[0])
distance[headNode[0]] = 0

print(S)
print(V)

while len(V) != 0 :
	minDistance = sys.maxsize
	pickedElement = 0
	for outerNode in V :
		for innerNode in S :
			if outerNode in adjacencyGraph[innerNode] :
				tmpDistance = distance[innerNode] + 1
				if tmpDistance < minDistance :
					minDistance = tmpDistance
					pickedElement = outerNode
	if (minDistance == sys.maxsize ) :
		print("Exiting with S of size " + str(len(S)))
		break
	distance[pickedElement] = minDistance
	print(" Picked element " + str(pickedElement) + " of distance " + str(minDistance))
	S.append(pickedElement)
	V.remove(pickedElement)
			


