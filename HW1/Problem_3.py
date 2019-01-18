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

def patternPlot():
    return
    
def plotData(data):
    
    l = len(data)
    
    for i in range(l):
        currData = data[i]
        lineType = currData[0]
        linePattern = currData[6]
        if (lineType == 1):
            currDataX = [currData[1], currData[3]]
            currDataY = [currData[2], currData[4]]
            if (linePattern == 1):
                plt.plot(currDataX, currDataY, 'k-')
            elif(linePattern == 3):
                return
                
        elif(currData[0] == 2):
            center = [currData[1],currData[2]]
               
    plt.show()
if __name__ == '__main__':
    textData = readText("2d-shape-1.txt")
    plotData(textData)