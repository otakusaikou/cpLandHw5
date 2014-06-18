#!/usr/bin/python2.7
from numpy import random, array, median
from resultPlotter import *

#This function read score data
def readData(filename):
    fin = open(filename)

    #Read score as numpy array, as type float
    data = array(fin.readlines()).astype(float)
    fin.close()

    return data

#This function returns statistics result of score
def classify(data, pattern = 1):
    ranks = {} 
    
    if pattern == 1:
        #Classify score data with 10 ranks
        for i in range(10):
            if i == 0:
                ranks['A'] = len(data[data >= 90])
            else:
                ranks[chr(65 + i)] = len(data[(data < (100 - i * 10)) & (data >= (100 - (i + 1) * 10))])
    else:
        #Classify score data with 6 ranks
        for i in range(5):
            if i == 0:
                ranks['A'] = len(data[data >= 90])
            elif i == 4:
                ranks["F"] = len(data[data < 60])
            else:
                ranks[chr(65 + i)] = len(data[(data < (100 - i * 10)) & (data >= (100 - (i + 1) * 10))])
    return ranks

def main():
    #For Question 1
    print "=" * 10 + "Reuslts of Question1" + "=" * 10
    data1 = readData("score.dat")
    
    #Classify data
    ranks1 =  classify(data1)
    
    #Print statistical result
    print "Max     = %6.2f\nMin     = %6.2f\nAverage = %6.2f\nMedian  = %6.2f\nStd.    = %6.2f\nVar.    = %6.2f" % (data1.max(), data1.min(), data1.mean(), median(data1), data1.std(), data1.var())
    
    #Plot results
    plotAsString(ranks1)
    plotHist(data1)
    print "=" * 10 + "Reuslts of Question1" + "=" * 10
    #For Question 2
    print "=" * 10 + "Reuslts of Question2" + "=" * 10
    data2 = random.randint(0, 101, 100)
    ranks2 =  classify(data2, 2)
    
    #Print statistical result
    print "Max     = %6.2f\nMin     = %6.2f\nAverage = %6.2f\nMedian  = %6.2f\nStd.    = %6.2f\nVar.    = %6.2f" % (data2.max(), data2.min(), data2.mean(), median(data2), data2.std(), data2.var())
    
    #Plot results
    plotAsString(ranks2)
    plotBar(ranks2, ("A", "B", "C", "D", "F"))
    print "=" * 10 + "Reuslts of Question2" + "=" * 10
    
    #Show all figure
    plt.show()
    
    return 0

if __name__ == "__main__":
    main()

