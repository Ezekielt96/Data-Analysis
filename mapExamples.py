
# Let say we have two columns read from a dataset
c =  [ [0,6, 19, 34, 15, 24, 8, 3 ], [ 54, 67, 8, 1, 34, 2, 89, 5 ] ]


# Want 8 sets of two items , the first item adds column 0 and column 1 together based on the row
# The second has the value True or False depending on if the first item is positive or not

#result = [ [54,True], ...


pairedSet = zip(c[0],c[1])
resultMap = {} 

for i in range(len(c[0])) :
	addedValues = c[0][i] + c[1][i]
	if addedValues %2 == 0 :
		resultMap[i] = [ addedValues,True]
	else : 
		resultMap[i] = [addedValues,False]







# I want to added the corresponding columns from the row index,
# The keys represent the modulus % 3 value where we are accumulating the sum

resultMap = {}
for i in range(len(c[0])) :
	addedValues = int(c[0][i]) + int(c[1][i])
	modulusValue = addedValues % 3 
	if modulusValue in resultMap.keys() :
		resultMap[modulusValue] += addedValues
	else :
		resultMap[modulusValue] = addedValues 


print(resultMap)

