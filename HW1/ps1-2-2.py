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

def saveToText(toSaveStrings, fileName):
    file = open(fileName, 'w')
    file.write(toSaveStrings)
    file.close()

def patternPlot(lineSegment):
    toReturn = ""
    lineType    = lineSegment[0]
    patternType = lineSegment[5]
    
    if lineType == 1:
        patternType = lineSegment[5]
        xPos = [lineSegment[1], lineSegment[3]]
        yPos = [lineSegment[2], lineSegment[4]]
        if patternType == 1: 
            currString = "1, %f, %f, %f, %f, 1, 0, 0 \n" % (xPos[0], yPos[0], xPos[1], yPos[1])
            toReturn = toReturn + currString
            plt.plot(xPos, yPos, 'k-')
            
        
        elif patternType == 3:
            width = lineSegment[6]
            pitch = lineSegment[7]
            direction = [xPos[1] - xPos[0], yPos[1] - yPos[0]]
            length = np.linalg.norm(direction)
            unitDir = direction / length
            orthUnitDir = [-unitDir[1], unitDir[0]]
            increment = pitch / 2
            currPos = [xPos[0], yPos[0]]
            currLength = 0
            
            # Start Step 1
            startIncrement = increment / 2.0
            nextPos = np.multiply(startIncrement, unitDir)
            nextPos = np.add(nextPos, np.multiply(orthUnitDir, width / 2.0))
            nextPos = np.add(currPos, nextPos)
            toPlotX = [currPos[0], nextPos[0]]
            toPlotY = [currPos[1], nextPos[1]]
            currString = "1, %f, %f, %f, %f, 1, 0, 0 \n" % (toPlotX[0], toPlotY[0], toPlotX[1], toPlotY[1])
            currLength += startIncrement
            plt.plot(toPlotX, toPlotY,'k-')
            currPos = nextPos
            overLength = 0
            counter = 1
            while (overLength != 1):
                
                if (currLength + increment > length):
                    overLength = 1
                    nextPos = [xPos[1], yPos[1]]
                else:
                    nextPos = np.add(currPos, np.multiply(increment, unitDir))
                    nextPos = np.add(nextPos, np.multiply(width * np.power(-1, counter), orthUnitDir))
                    
                toPlotX = [currPos[0], nextPos[0]]
                toPlotY = [currPos[1], nextPos[1]]
                counter += 1
                currPos = nextPos
                currLength += increment
                plt.plot(toPlotX, toPlotY, 'k-')
            
        
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
                toReturn += "1, %f, %f, %f, %f, 1, 0, 0 \n" % (xPos[0], yPos[0], xPos[1], yPos[1])
                plt.plot(xPos, yPos, 'k-')
                
        elif patternType == 3:
            width = lineSegment[-2]
            pitch = lineSegment[-1]
            currAng = theta[0]
            currPos = [np.cos(currAng * np.pi) * r, np.sin(currAng * np.pi) * r]
            currPos = np.add(currPos, centerPos)
            increment = np.arcsin((pitch / 2) / r)  / np.pi
            angleRange = np.abs(lineSegment[4] - lineSegment[5])
            
                
            
            startIncrement = increment / 2
            currAng += startIncrement
            nextPos = [np.cos(currAng * np.pi) * r, np.sin(currAng * np.pi) * r]
            orthUnitDir = np.divide(nextPos, np.linalg.norm(nextPos))
            nextPos = np.add(nextPos, centerPos)
            posChange = np.multiply(width / 2.0, orthUnitDir)
            nextPos = np.add(nextPos, posChange)
            toPlotX = [currPos[0], nextPos[0]]
            toPlotY = [currPos[1], nextPos[1]]
            currString = "1, %f, %f, %f, %f, 1, 0, 0 \n" % (toPlotX[0], toPlotY[0], toPlotX[1], toPlotY[1])
            plt.plot(toPlotX, toPlotY, 'k-')
            toReturn += currString
            currAngleSpan = startIncrement
            overAngle = 0
            counter = 1
            currPos = nextPos
            
            while (overAngle != 1):
                
                if (currAngleSpan + increment > angleRange):
                    overAngle = 1
                    currAng = theta[1]
                    nextPos = [np.cos(currAng * np.pi) * r, np.sin(currAng * np.pi) * r]
                    nextPos = np.add(nextPos, centerPos)
                else:
                    currAng += increment
                    nextPos = [np.cos(currAng * np.pi) * r, np.sin(currAng * np.pi) * r]
                    orthUnitDir = np.divide(nextPos, np.linalg.norm(nextPos))
                    nextPos = np.add(nextPos, centerPos)
                    posChange = np.multiply(np.power(-1, counter), orthUnitDir)
                    posChange = np.multiply(posChange, width / 2.0)
                    nextPos = np.add(nextPos, posChange)
                
                toPlotX = [currPos[0], nextPos[0]]
                toPlotY = [currPos[1], nextPos[1]]
                currString = "1, %f, %f, %f, %f, 1, 0, 0 \n" % (toPlotX[0], toPlotY[0], toPlotX[1], toPlotY[1])
                plt.plot(toPlotX, toPlotY, 'k-')
                toReturn += currString 
                counter += 1
                currPos = nextPos
                currAngleSpan += increment
                    
                    
            
            
            
            
        
    return toReturn
    
def handlePlot(data):
    toReturn = ""
    l = len(data)
    
    for i in range(l):
        currData = data[i]
        tempString = patternPlot(currData)
        toReturn += tempString
                         
    plt.show()
    return toReturn
    
if __name__ == '__main__':
    textData = readText("2d-shape-1.txt")
    stringsToSave = handlePlot(textData)
    saveToText(stringsToSave, 'output_shape_1.txt')