# Developer Ezekiel D Towner 
# File Reader
# Project # 1
# This program reads in a csv file, then find the average GRE score
# The second column is the GRE score


import csv

greSet = []
with open('Admission_Predict.csv') as csv_file:
	csvReader = csv.reader(csv_file,delimiter=',')
	for index, lineSet in enumerate(csvReader) :
		if index == 0 :
			# not reading the header line
			continue
		greSet.append(int(lineSet[1]))
accumulateValue  = 0
for greScore in greSet :
	accumulateValue += greScore

#accumulateValue = [ x for x in greSet ] 

avgScore = accumulateValue / len(greSet)

print(greSet,avgScore)




