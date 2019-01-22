'''
Created on Jan 20, 2019

@author: Grant Zheng
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

arm1 = 125
arm2 = 225
hand = 61.5
initZ = 312
baseWidth = 150
baseLength = 192
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlim(-500, 500)
ax.set_ylim(-500, 500)
ax.set_zlim(0, 1000)
joint1Limit = np.deg2rad(155) / np.pi
joint2Limit = np.deg2rad(145) / np.pi

def calculateVector(angle):
    return [-np.sin(angle * np.pi), np.cos(angle * np.pi)]

def handleKinematics(userInputs):
    joint1 = calculateVector(userInputs[0]) * arm1
    joint2 = calculateVector(userInputs[1]) * arm2
    joint2 += joint1
    
    handTheta = userInputs[0] + userInputs[1] + userInputs[3]
    return [joint2[0], joint2[1], initZ - userInputs[2], handTheta]
 

       
def handleUI():
    toReturn = input("Enter numbers, separate by comma \n>> ")
    toReturn = toReturn.split(",")
    toReturn = list(map(float, toReturn))
    theta1 = toReturn[0]
    theta2 = toReturn[1]
    
    if np.abs(theta1) > joint1Limit:
        raise ValueError('Joint 1 angle out of range, enter value between %f and %f' % (-joint1Limit, joint1Limit))
    elif np.abs(theta2) > joint2Limit:
        raise ValueError('Joint 2 angle out of range, enter value between %f and %f' % (-joint2Limit, joint2Limit))
    elif len(toReturn) != 4:
        raise IndexError('Enter 4 numbers, separate by comma')
    return toReturn

def plotRectangle(corners):
    baseX = []
    baseY = []
    baseZ = []
    for i in range(len(corners)):
        baseX.append(corners[i][0])
        baseY.append(corners[i][1])
        baseZ.append(corners[i][2])
    baseX.append(corners[0][0])
    baseY.append(corners[0][1])
    baseZ.append(corners[0][2]) 
    baseX = np.array([baseX])
    baseY = np.array([baseY])
    baseZ = np.array([baseZ])
    ax.plot_wireframe(baseX, baseY, baseZ)
    
def plotCircles(center, radius):
    toPlotX = []
    toPlotY = []
    toPlotZ = []
    
    increment = 2 * np.pi / 100
    for i in range(100):
        toPlotX.append(center[0] + np.cos(i * increment) * radius)
        toPlotY.append(center[1] + np.sin(i * increment) * radius)
        toPlotZ.append(center[2])
        
    toPlotX.append(center[0] + np.cos(0 * increment) * radius)
    toPlotY.append(center[1] + np.sin(0 * increment) * radius)
    toPlotZ.append(center[2]) 
    
    toPlotX = np.array([toPlotX])
    toPlotY = np.array([toPlotY])
    toPlotZ = np.array([toPlotZ])
    ax.plot_wireframe(toPlotX, toPlotY, toPlotZ) 
    
def plotLine(startPos, endPos):
    toPlotX = [startPos[0], endPos[0]]
    toPlotY = [startPos[1], endPos[1]]
    toPlotZ = [startPos[2], endPos[2]]
    toPlotX = np.array([toPlotX])
    toPlotY = np.array([toPlotY])
    toPlotZ = np.array([toPlotZ])
    ax.plot_wireframe(toPlotX, toPlotY, toPlotZ)
     
    
      
    
def handelPlot(operationPos):
    c1 = [75,75,0]
    c2 = [-75, 75, 0]
    c3 = [-75, -192,0]
    c4 = [75, -192,0]
    plotRectangle([c1,c2,c3,c4])
    baseLoc = [0,0,0]
    currLoc = np.matrix([[0],
                         [0],
                         [0],
                         [1]])
    
    moveToJoint1 = np.matrix([[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 1, 566],
                              [0, 0, 0, 1]])
    joint1Pos = np.matmul(moveToJoint1, currLoc)
    joint1Pos = [joint1Pos.item((0,0)),joint1Pos.item((1,0)),joint1Pos.item((2,0))]
    plotLine(baseLoc, joint1Pos)
    plotCircles(baseLoc, 25)
    
    plotCircles(joint1Pos, 25)
    arm1Vec = np.matrix([[0],
                         [arm1],
                         [0],
                         [1]])
    theta1 = operationPos[0] * np.pi
    rotateArm1 = np.matrix([[np.cos(theta1), -np.sin(theta1), 0, 0],
                            [np.sin(theta1), np.cos(theta1), 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])
    joint2Pos = np.matmul(rotateArm1, arm1Vec)
    joint2Pos = np.matmul(moveToJoint1, joint2Pos)
    joint2Pos = [joint2Pos.item((0,0)),joint2Pos.item((1,0)),joint2Pos.item((2,0))]
    plotLine(joint1Pos, joint2Pos)
    plotCircles(joint2Pos, 25)
    
    arm2Vec = np.matrix([[0],
                         [arm2],
                         [0],
                         [1]])
    theta2 = operationPos[1] * np.pi
    rotateArm2 = np.matrix([[np.cos(theta2), -np.sin(theta2), 0, 0],
                            [np.sin(theta2), np.cos(theta2), 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])
    moveToArm2 = np.matrix([[1, 0, 0, 0],
                            [0, 1, 0, arm1],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])
    
    joint2Trans = np.matmul(moveToJoint1, rotateArm1)
    joint2Trans = np.matmul(joint2Trans, moveToArm2)
    joint2Trans = np.matmul(joint2Trans, rotateArm2)
    joint3Pos = np.matmul(joint2Trans, arm2Vec)
    joint3Pos = [joint3Pos.item((0,0)),joint3Pos.item((1,0)),joint3Pos.item((2,0))]
    plotLine(joint2Pos, joint3Pos)
    plotCircles(joint3Pos, 25)
   
    moveDown =  np.matrix([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, -operationPos[2]],
                           [0, 0, 0, 1]])
    moveToHand = np.matrix([[1, 0, 0, 0],
                           [0, 1, 0, arm2],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
    
    joint3Trans = np.matmul(joint2Trans, moveToHand)
    joint3Trans = np.matmul(joint3Trans, moveDown)
    downVect = np.matrix([[0],
                         [0],
                         [0],
                         [1]])
    handPos = np.matmul(joint3Trans, downVect)
    handPos = [handPos.item((0,0)),handPos.item((1,0)),handPos.item((2,0))]
    rodEnd = [handPos[0], handPos[1], handPos[2] + 697 - 246]
    plotLine(rodEnd, handPos)
    
    handVect = np.matrix([[0],
                         [hand],
                         [0],
                         [1]])
    theta3 = -operationPos[-1] * np.pi
    handTrans = np.matrix([[np.cos(theta3), -np.sin(theta3), 0, 0],
                            [np.sin(theta3), np.cos(theta3), 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])
    handTrans = np.matmul(joint3Trans, handTrans)
    handOrt  = np.matmul(handTrans, handVect)
    finalPos = [handOrt.item((0,0)),handOrt.item((1,0)),handOrt.item((2,0))]
    plotLine(handPos, finalPos)
if __name__ == '__main__':
    userInput = handleUI()
    handelPlot(userInput)
    plt.show()
    