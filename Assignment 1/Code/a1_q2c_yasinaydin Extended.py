def lcs(X,Y,i,j):
    if (i == 0 or j == 0):
        return 0
    elif X[i-1] == Y[j-1]:
        return 1 + lcs(X,Y,i-1,j-1)
    else:
        return max(lcs(X,Y,i,j-1),lcs(X,Y,i-1,j))
#Figure 1: A recursive algorithm to compute the LCS of two strings

def lcs2(X,Y,i,j):
    if c[i][j] >= 0:
        return c[i][j]
    if (i == 0 or j == 0):
        c[i][j] = 0
    elif X[i-1] == Y[j-1]:
        c[i][j] = 1 + lcs2(X,Y,i-1,j-1)
    else:
        c[i][j] = max(lcs2(X,Y,i,j-1),lcs2(X,Y,i-1,j))
    return c[i][j]
#Figure 2: A recursive algorithm to compute the LCS of two strings, with memoization

###########################################################

import random
import time
import numpy as np
import matplotlib.pyplot as plt
from statistics import stdev 
import math

dnaNucleotides = ["A","G","C","T"]
#lengthList = [ 6, 8, 10, 12, 14]
lengthList = [ i for i in range(500)]
cols = len(lengthList)
testAmount = 30
recordedTimesMemoization = [[0]*cols]*testAmount

for i in range(30):
    print("Test id:",i)
    for idxOfList in range(len(lengthList)):
        #creating sequence
        randomSequence1=''
        randomSequence2=''
        for j in range(0,lengthList[idxOfList]):
            randomSequence1 += random.choice(dnaNucleotides)
            randomSequence2 += random.choice(dnaNucleotides)
        lX = len(randomSequence1)
        lY = len(randomSequence2)
        
        startTime = time.time()
        c = [[-1 for k in range(lY+1)] for l in range(lX+1)]
        lcs2(randomSequence1, randomSequence2, lX, lY)
        endTime = time.time()
        recordedTimesMemoization[i][idxOfList] = endTime-startTime
        print("Memoization with m=n="+str(lengthList[idxOfList])+" =>",endTime-startTime)

memoizationMeanList = []
memoizationStdList = []

print("Memoization mean/std:")
for n in range(len(lengthList)):
    mean = 0
    for i in range(testAmount):
        mean += recordedTimesMemoization[i][n]
    mean = mean / len(lengthList)
    memoizationMeanList.append(mean)
    meanDiff = 0
    for i in range(testAmount):
        meanDiff += pow((mean-recordedTimesMemoization[i][n]),2)
    std = math.sqrt(meanDiff/(len(lengthList)-1))
    memoizationStdList.append(std)
    print(lengthList[n], "mean:", mean, "std:", std)

plt.plot(lengthList,memoizationMeanList,linewidth=2.0)
plt.xlabel('input size')
plt.ylabel('runtime (memoization)')
plt.show()
