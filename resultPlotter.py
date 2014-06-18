import matplotlib.pyplot as plt
from numpy import arange

#This function plot data distribution with string
def plotAsString(data):
    #Show results with numbers 
    for key in sorted(data.iterkeys()):
        print "%s : %d" % (key, data[key])
    
    #Show results with '*' sign 
    for key in sorted(data.iterkeys()):
        print "%s :" % key, "*" * data[key]

#This function plot data distribution with graphic tools
def plotHist(data):
    plt.figure("Histogram")

    #Create bins 
    bins = [x for x in range(0, 101, 10)]
    
    #Plot histogram
    plt.hist(data, bins)
 
    #Set the labels
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    
    #Set view range   
    plt.xlim([0, 100])
    
#This function plot bar chat with input data
def plotBar(data, rankLabel):
    plt.figure("Barchart")
    
    #Set rank label
    index = arange(len(data))
    plt.xticks(index + 0.5, rankLabel)
    
    #Set the labels
    plt.xlabel("Rank")
    plt.ylabel("Number of Students")
    
    #Get values
    values = []
    for key in sorted(data.iterkeys()):
        values.append(data[key])
        
    #Plot barchart
    bar_width = 1
    plt.bar(index, values, bar_width)
    
    #Set view range
    plt.xlim([0, len(data)])