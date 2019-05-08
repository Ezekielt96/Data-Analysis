# Put the odd numbers within a list

import csv

a = [ 23, 5, [23, 2], 16, 27, 9, 12, 56, 67, 89 ]


c = [ x for index,x in enumerate(a) if index != 2 and x % 2 == 1 ]

# HERE WE POPULATED THE WORDSET, THIS IS A SET OF SETS
with open('Admission_Predict.csv') as readObject :
    #for line in readObject :
    #   lineSet = line.strip().split(',')
#   wordSet = [ ['1', '13'], [  .... ] ]
    wordSet = []
    for index,line in enumerate(readObject) :
        if index == 0 : 
            continue
        wordSet.append( [word for word in line.strip().split(',')] )

    for line in wordSet :
            for index, word in enumerate (line) :
                line[index] = float(line[index])
print(wordSet)
#Find the std for each element 
