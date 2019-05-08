# Breadth first search 


import queue
import random

# put -- adds an element to the end of a queue
# get -- return and removes an element from the head of the queu



#graph = [ [4,3 ], [2,4 ], [4,0,1], [4,2,1] ,[1,2,3] ]

#adjacencyList = {}
#for index,neighborList in enumerate(graph) :
#	adjacencyList[index] = neighborList

adjacencyList = {}
numNodes = 10
for index in range(numNodes) :
	neighborSize = random.sample(range(3,8),1)
	neighborList = random.sample(range(1,10),neighborSize[0])
	if index in neighborList :
		neighborList.remove(index)
	if index != 0 :
		if 0 in neighborList :
			neighborList.remove(0)
	adjacencyList[index] = neighborList

#print(adjacencyList)

adjacencyList = {}

inputFile = open("output.csv",'r') 
for line in inputFile :
	tokenizedLine = line.strip().split(',')
	tmpList = []
	key =  -1
	for index,element in enumerate(tokenizedLine) :
		if index == 0 :
			key = int(element)
		else :
			tmpList.append(int(element))
	adjacencyList[key] = tmpList

inputFile.close()


print(adjacencyList)
			

# Let put these elements into a map

# add the head element onto the queue
# while the queue is empty
	# pop an element out of the queue
	# queue the popped element's neighbors

myStack = []   # myStack.insert(0,node)
myStack.append(0)

# If a queue  -- myStack.append(node)


count = 0
visitedList = []
while len(myStack) != 0 :
	element = myStack.pop()
    # Check if element is in the visited list if so continue
	if element in visitedList :
		continue	

	# Add the element to the visited list
	for index,node in enumerate(adjacencyList[element]) :
		if element in visitedList :
			myStack.insert(0,node)
	print(element)
	# 







