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

lengthList = [ 6, 10, 12, 14, 16]
recordedTimesNaive = []
recordedTimesMemoization = []
mainSequence1 = "aaaaaaaaaaaaaaaaaaaaaaaaa"
mainSequence2 = "ttttttttttttttttttttttttt"

for length in lengthList:
    #creating sequence
    sequence1=mainSequence1[0:length]
    sequence2=mainSequence2[0:length]

    startTime = time.time()
    lcs(sequence1, sequence2, length, length)
    endTime = time.time()
    recordedTimesNaive.append(endTime-startTime)
    print("Naive with m=n="+str(length)+" =>",endTime-startTime)

    startTime = time.time()
    c = [[-1 for k in range(length+1)] for l in range(length+1)]
    lcs2(sequence1, sequence2, length, length)
    endTime = time.time()
    recordedTimesMemoization.append(endTime-startTime)
    print("Memoization with m=n="+str(length)+" =>",endTime-startTime)

plt.plot(lengthList,recordedTimesNaive,linewidth=2.0)
plt.xlabel('input size')
plt.ylabel('runtime (naive recursive)')
plt.show()

plt.plot(lengthList,recordedTimesMemoization,linewidth=2.0)
plt.xlabel('input size')
plt.ylabel('runtime (memoization)')
plt.show()
