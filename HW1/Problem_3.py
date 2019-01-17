'''
Created on Jan 17, 2019

@author: Grant Zheng
'''
import matplotlib.pyplot as plt

def readText(fileName):
    currFile = open(fileName, 'r')
    currFile = currFile.read()
    splittedFile = currFile.split("\n")
    toReturn = []
    l = len(splittedFile)
    for i in range(l):
        
        try:
            firstChar = splittedFile[i][0]
            if (firstChar.isdigit()):
                toReturnList = list(map(int, splittedFile[i].split(",")))
                toReturn.append(toReturnList)
        
        except:
            pass

    
    return toReturn

def plotData(data):
    
    l = len(data)
    
    for i in range(l):
        if (data[i][0] == 1):
            toPlotData = data[i][1:5]
            plt.plot(toPlotData)
            print(toPlotData)
        
    plt.show()
if __name__ == '__main__':
    textData = readText("2d-shape-1.txt")
    plotData(textData[0:2])