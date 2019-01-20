'''
Created on Jan 17, 2019

@author: Grant Zheng
'''
import matplotlib.pyplot as plt
import numpy as np


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
            length = np.linalg.norm(direction)
            unitDir = direction / length
            orthUnitDir = [-unitDir[1], unitDir[0]]
            increment = pitch / 4.0
            currPos = [xPos[0], yPos[0]]
            nextPos = [-1, -1]
            overLength = 0
            currLength = 0
            counter = 0
            patternDir = 1
            
            while (overLength != 1):
                
                if (currLength + increment >= length):
                    overLength = 1
                    nextPos = [xPos[1], yPos[1]]
                   
                    
                else:
                    rmd = counter % 4
                    
                    if (rmd == 0 or rmd == 3):
                        patternDir = 1
                    else:
                        patternDir = -1
                        
                    nextPos = np.add(currPos, np.multiply(unitDir, increment))
                    nextPos = np.add(nextPos, np.multiply(patternDir * width / 2.0, orthUnitDir))
                toPlotCurr = [currPos[0], nextPos[0]]
                toPlotNext = [currPos[1], nextPos[1]]
                plt.plot(toPlotCurr, toPlotNext, 'k-')
                currPos = nextPos
                counter += 1
                currLength += increment
            
        
    elif lineType == 2:
        patternType = lineSegment[6]
        resolution = 100
        centerPos = lineSegment[1:3]
        r         = lineSegment[3]
        theta     = lineSegment[4:6] 
        
        if patternType == 1:
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
            width = lineSegment[-2]
            pitch = lineSegment[-1]
            currAng = theta[0]
            currPos = [np.cos(currAng * np.pi) * r, np.sin(currAng * np.pi) * r]
            currPos = np.add(currPos, centerPos)
            nextPos = [-1, -1]
            nextAng = -1
            angleSpan = theta[1] - theta[0]
            totAng = 0
            increment = np.arcsin((width / 2) / r) / 2 / np.pi
            if (theta[1] < theta[0]):
                angleSpan = 2 + angleSpan
                
            overAngle = 0
            counter = 0
            while(overAngle != 1):
                
                if (totAng + increment > angleSpan):
                    overAngle = 1
                    nextAng = theta[1]
                    nextPos = [np.cos(nextAng * np.pi) * r,  np.sin(nextAng * np.pi) * r]
                    nextPos = np.add(nextPos, centerPos)
                else:
                    nextAng = currAng + increment
                    nextPos = [np.cos(nextAng * np.pi) * r,  np.sin(nextAng * np.pi) * r]
                    nextPos = np.add(nextPos, centerPos)
                    orthDir = np.subtract(nextPos, centerPos)
                    unitOrthDir = orthDir / np.linalg.norm(orthDir)   
                         
                    if (counter % 4 == 2):
                        nextPos = np.add(nextPos, unitOrthDir * width / 2)
                    elif(counter % 4 == 0):
                        nextPos = np.subtract(nextPos, unitOrthDir * width / 2)
                    
                toPlotX = [currPos[0], nextPos[0]]
                toPlotY = [currPos[1], nextPos[1]]
                currPos = nextPos
                   
                    
                plt.plot(toPlotX, toPlotY, 'k-')
                counter += 1
                totAng += increment
                currAng = nextAng
            
        
        
    
def handlePlot(data):
    
    l = len(data)
    
    for i in range(l):
        currData = data[i]
        patternPlot(currData)
                         
    plt.show()
    
if __name__ == '__main__':
    textData = readText("2d-shape-2.txt")
    handlePlot(textData)