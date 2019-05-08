# Depth first search 


adjacencyList = {}
visitedList = [0]

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

# Remember that n is a instance of node that has the path in it
def dfs(n) :
	# Iterate over all the vistedList node objects testing for n.nodeId and item.nodeId
	if item in visitedList :
		return
	
	# We are append node instance
	# Instead of n , specify the node item
	visitedList.append(n)
	for n_node in adjacencyList[n] :
		if n_node not in visitedList :
			# This is n.nodeItem
			for n_node in adjacencyList[n] :
				# Create an instance of n_node 
				# n_node.nodeId = n_node
                # n_node.myPath = n.myPath
                # n_node.myPath.append(n_node.nodeId)
				dfs(n_node) 



for nodeKey in adjacencyList[0] :
	# nodeInstance = Node(id, path - [sourceNode, nodeKey]
	dfs(nodeKey)




# Example of how to create a class node 

class Node :
	def __init__(self,id) :
		self.nodeId = id

print(visitedList)

nodeVisitedList = []
for i in visitedList :
	instanceObject = Node(i)
	nodeVisitedList.append(instanceObject)


for element in nodeVisitedList :
	print(element.nodeId)

	
