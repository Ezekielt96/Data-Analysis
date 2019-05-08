# Put the odd numbers within a list

import csv

a = [ 23, 5, [23, 2], 16, 27, 9, 12, 56, 67, 89 ]


c = [ x for index,x in enumerate(a) if index != 2 and x % 2 == 1 ]


# HERE WE POPULATED THE WORDSET, THIS IS A SET OF SETS
with open('Admission_Predict.csv') as readObject :
	#for line in readObject :
	#	lineSet = line.strip().split(',')
#	wordSet = [ ['1', '13'], [  .... ] ]
	wordSet = []
	for index,line in enumerate(readObject) :
		if index == 0 : 
			continue
		wordSet.append( [word for word in line.strip().split(',')] )


	for line in wordSet :
		for index,word in enumerate(line) :
			line[index] = float(line[index])


# For each column find the average value 

# INITLIALING THE SET  - avgList  where each column is set to 0
avgList = []
columnCount = 0 
for line in wordSet :
	columnCount = len(line)
	continue

for i in range(columnCount) :
	avgList.append(0)


# AGGREGATING EACH VALUE THAT IS IN THE SAME COLUMN
#avgList -> [ total GRE/rowCount , total TOFL/rowCount , ...  ] 
for line in wordSet :
	for index,value in enumerate(line) :
		# index represents the column 
		# print(index,value)
		avgList[index] += value

#print(avgList,len(wordSet))
	
# Here we have len(wordSet) is equal to the number of rows
# Divide the the column count over the number of rows to find the average
for index in range(len(avgList)) :
	avgList[index] = avgList[index] / len(wordSet)


print(avgList)


### Lets find the std for each element of the GRE score
##sdevList = [ [     ] ,  [     ]]
##
##for col in range(columnCount) :
##	emptySet = []
##	sdevList.append(emptySet)
##
### Standard deviation is the value minus avg value squared
##for line in wordSet :
##        for index,value in enumerate(line):
##		if ( index == 0 ):
##			continue
##		
##		stDev = abs(avgList[index] - value)
##		sdevList[index].append(stDev)
##
##
##print(sdevList)
##
##
##
##
##matrixData = [ [1,3,5,6],[2,34,6,57]]
##transposeMatrix = []
##for i in range(4) :
##	transposeMatrix.append([ row[i] for row in matrixData])
##
##
##
##fnAdd = lambda x,y,z : x + y + z
##
##print(fnAdd(2,3,5))
##
##def addFn(x,y,z) :
##	return x + y + z
##
##
##addFn(15,12,4)
##
##
###print(transposeMatrix)
##
