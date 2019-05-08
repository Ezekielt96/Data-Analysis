
mySet = [ 12, 4, 7, 6, 8, 10, 23, 15 ]


#for value in mySet :
#	if value % 2 == 1 :
#		print(value)

def findOddValues(currSet) :
	oddSet = [ value for value in currSet if value % modulusNumber == 0 ] 
	return oddSet


newSet = findOddValues(mySet)

modulusNumber  = 3
print(newSet)



