# Developer Ezekiel Towner
# Programming For Data Analysis
# Project 1 
# This program opens a CSV file and prints the average value  

import csv

# HERE WE POPULATED THE WORDSET, THIS IS A SET OF SETS
with open('Admission_Predict.csv') as readObject :
    #for line in readObject :
      #lineSet = line.strip().split(',')
  #wordSet = [ ['1', '13'], [  .... ] ]
    wordSet = []
    for index,line in enumerate(readObject) :
        if index == 0 : 
            continue
        wordSet.append( [word for word in line.strip().split(',')] )

    for line in wordSet :
            for index, word in enumerate (line) :
                line[index] = float(line[index])

#*****************************************************************************

#For each column find the average value
avgList = []
columCount = 0
for line in wordSet :
    columnCount = len(line)
    continue

for i in range (columnCount):
    avgList.append(0)
    
#[0,0,0,0,0]
print (avgList, len(wordSet))

#avgList -> [ [totalNumber/rowCount],total TOFL/rowCount, ...]
for line in wordSet:
    for index,value in enumerate(line):
        #index represents the column
        #print(index,value)
        avgList[index] += value

#print(avgList,len(wordSet))
	
# Here we have len(wordSet) is equal to the number of rows
# Divide the the column count over the number of rows to find the average
for index in range(len(avgList)) :
	avgList[index] = avgList[index] / len(wordSet)

#*************************************************************************
#STANDARD DEVIATION


sdevList = [[ ], [    ] ]

for col in range(columnCount) :
    emptySet = []
    sdevList.append(emptySet)
#The Standard deviation is the value minus avg value Squared 
for line in wordSet :
            for index, value in enumerate (line) :
                if (index == 0 ) :
                    continue 
                stDev = pow (avgList[index]-value,2)
                stdGreValue = sdevList[index]
                sdevList[index].append(stDev)

print("")
print("Average:")
#Prints out average value of all 400 items in list from all 9 coloumns 
print(avgList)
print("")
print("")
print ("Standard Deviation:")
for index, column in enumerate (sdevList):
    #Standard deviation list for GRE
    if (index == 1):
        print(column)
#*******************************************************************************
#MAX VALUE
maxList = []
maxCount = 0
for line in wordSet:
    maxCount = len(line)
    continue
for x in range (maxCount):
    maxList.append(0)

print (maxList, len(wordSet)) # length in wordSet is 400 total

##using max funtion to iterate through list
##PRINTS OUT HIGHEST ROW IN EXCEL SPREADSHEET 
for y in range(0, len(wordSet), 1):
    maxList = max(maxList,wordSet[y])

def findMan(i) :
    maxCol = 0
    for dataItem in dataColumn [i ] :
        if dataItem < maxCol :
             maxCol = dataItem
        return maxCol
print ()



print ("")
print ("")
print ("Max Column:")
print(maxList)
##****************************************************************************************
#MIN VALUE
minimum = wordSet[0]
for number in wordSet:
    if minimum > number:
        minimum = number
print ("")
print ("")
print ("Min Column:")
print (minimum)

def findMin(i) :
    minCol = 100000 
    for dataItem in dataColumn [i] :
        if dataItem < minCol :
             minCol = dataItem
        return minCol
print (i)


    
    


