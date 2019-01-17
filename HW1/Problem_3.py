'''
Created on Jan 17, 2019

@author: Grant Zheng
'''

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


if __name__ == '__main__':
    print(readText("2d-shape-1.txt")[0])