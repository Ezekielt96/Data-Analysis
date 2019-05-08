
# Let say we have two columns read from a dataset
c =  [ [0,6, 19, 34, 15, 24, 8, 3 ], [ 54, 67, 8, 1, 34, 2, 89, 5 ] ]


# Want 8 sets of two items , the first item adds column 0 and column 1 together based on the row
# The second has the value True or False depending on if the first item is positive or not

#result = [ [54,True], ...


pairedSet = zip(c[0],c[1]) 
resultSet = []
for i in range(len(c[0])) :
	resultSet.append([0,0])


newSet = [[0,0]] * len(c[0])

resultSet[2][1] += 1	
print(resultSet)

newSet[2][1] += 1 
print(newSet)


for index,item in enumerate(pairedSet) :
	addedValue = item[0] + item[1]
	isTrue = False
	if addedValue % 2  == 0 :
		isTrue = True
	resultSet[index][0] = addedValue
	resultSet[index][1] = isTrue



print(resultSet)
