'''
Created on Jan 17, 2019

@author: Grant Zheng
'''
import matplotlib.pyplot as plt
import numpy as np
import math

def readText(fileName):
    currFile = open(fileName, 'r')
    currFile = currFile.read()
    splittedFile = currFile.split("\n")
    toReturn = []
    l = len(splittedFile)
    for i in range(l):
        
        if (len(splittedFile[i]) != 0):
            firstChar = splittedFile[i][0]
            if (firstChar.isdigit()):
                toReturnList = list(map(float, splittedFile[i].split(",")))
                toReturn.append(toReturnList)
        
        

    
    return toReturn

def patternPlot(lineSegment):
    
    lineType    = lineSegment[0]
    patternType = lineSegment[5]
    
    
        
    if lineType == 1:
        patternType = lineSegment[5]
        xPos = [lineSegment[1], lineSegment[3]]
        yPos = [lineSegment[2], lineSegment[4]]
        if patternType == 1: 
            plt.plot(xPos, yPos, 'k-')
        
        elif patternType == 3:
            width = lineSegment[6]
            pitch = lineSegment[7]
            direction = [xPos[1] - xPos[0], yPos[1] - yPos[0]]
            unitDir = direction / np.linalg.norm(direction)
            orthUnitDir = [-unitDir[1], unitDir[0]]
            itr = np.linalg.norm(direction) / pitch
            itr = math.floor(itr)
            increment = pitch / 1.0 / 4.0
            startPos = [xPos[0], yPos[0]]

            for i in range (itr):
                currSeg = i * pitch * unitDir + startPos
                currLoc = currSeg
                for j in range(4):
                    nextLoc = np.add(np.multiply(increment, unitDir), np.multiply(math.pow(-1, j) * (width / 2), orthUnitDir))
                    nextLoc = np.add(currLoc, nextLoc)
                    toPlotX = [currLoc[0], nextLoc[0]]
                    toPlotY = [currLoc[1], nextLoc[1]]
                    currLoc = nextLoc
                    plt.plot(toPlotX, toPlotY, 'k-')
                     
                #print("new Pattern")
            print(direction)
        
    elif lineType == 2:
        patternType = lineSegment[6]
        resolution = 100
        
        if patternType == 1:
            centerPos = lineSegment[1:3]
            r         = lineSegment[3]
            theta     = lineSegment[4:6] * 180
            increment = (theta[1] - theta[0]) / resolution
            
            for i in range(100):
                ang = theta[0] + increment * i
                x1 = centerPos[0] + r * np.sin(np.pi * ang)
                x2 = centerPos[0] + r * np.sin(np.pi * (ang + increment))
                y1 = centerPos[1] + r * np.cos(np.pi * ang)
                y2 = centerPos[1] + r * np.cos(np.pi * (ang + increment))
                xPos = [x1, x2]
                yPos = [y1, y2]
                plt.plot(xPos, yPos, 'k-')
        elif patternType == 3:
            print("do")
        
        
    
def handlePlot(data):
    
    l = len(data)
    
    for i in range(l):
        currData = data[i]
        patternPlot(currData)
                         
    plt.show()
    
if __name__ == '__main__':
    textData = readText("2d-shape-1.txt")
    handlePlot(textData)