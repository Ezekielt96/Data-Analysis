import random


gradeList = []

for i in range(8) :
	floatValue = float(random.sample(range(1,3),1)[0])
	floatValue *= .3
	scoreList = random.sample(range(0,10),10)
	newList = []
	for i in scoreList :
		newList.append(i * floatValue)
	gradeList.append(newList)

print(gradeList)


# Write a program to calculate the avg score based on some column of values


def calcAvg(listOfScores,i) :
	accumScore = 0 
	for score in listOfScores :
		accumScore += score

	avgScore = accumScore / len(listOfScores)
	print("The avg score of column  " + str(i) + " is " + str(avgScore))
	return avgScore


# Write a program to calculate the standard deviation based on some column
def calcStd(listOfScores,i,avg) :
	varianceList = []
	# WE ARE GOING THE SUMMATION  (score - average) for each entry
	for score in listOfScores :
		varianceValue = pow(score-avg,2)
		varianceList.append(varianceValue)

	deviationValue = 0.0
	for variance in varianceList :
		deviationValue += variance

	stdDev = pow(deviationValue/(len(varianceList) -1) , .5)
	print("The standard deviation of column  " + str(i) + " is " + str(stdDev))
	return stdDev


# Write a program to calculate the values that are within the std deviation of the average score, and print the values of those that are not within that range
def findAvgValueRange(stdDev,listOfScores, myAvg) :
	acceptedList  = []
	rejectedList = []
	for score in listOfScores :
		if (score < (myAvg + stdDev)) and (score > (myAvg - stdDev)) :
			acceptedList.append(score)
		else :
			rejectedList.append(score)
	return(acceptedList,rejectedList)
	


		

myAvg = calcAvg(gradeList[2], 2)
stdDev = calcStd(gradeList[2],2,myAvg)
listTouple = findAvgValueRange(stdDev,gradeList[2],myAvg)
print(listTouple)
# Write a program to find which column has the highest standard deviation
highDeviation = 0
foundColumn = 0
# ITERATING OVER THE SUBSETS  (columns) in this loop - gradeList[columnIndex]  is a column
for columnIndex in range(len(gradeList)) :
	myAvg = calcAvg(gradeList[columnIndex],columnIndex)
	stdDev = calcStd(gradeList[columnIndex],columnIndex,myAvg)
    # IF THE CURRENT CALCUATED STD IS HIGHER THEN USE THIS AS THE NEW HIGH - STD
	if stdDev > highDeviation :
		highDeviation = stdDev
		foundColumn = columnIndex


print(" The column with highest std  is " + str(foundColumn) + " STD " + str(highDeviation))


