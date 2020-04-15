# Python program to find min cost path
# from station 0 to station N-1

def minCostRec(costMatrix, s, d):
    if len(costMatrix) < 3:  # for case of no city and 1 city existing
        return 0
    if s == d or s+1 == d:
        return costMatrix[s][d]

    min = costMatrix[s][d]

    for i in range(s+1, d):
        c = minCostRec(costMatrix, s, i) + minCostRec(costMatrix, i, d)
        if c < min:
            min = c
    return min

def minCost(costMatrix, startStation, targetStations):

    busEndCost = minCostRec(costMatrix, startStation, targetStations[0])  # ends up at the bus station
    trainEndCost = minCostRec(costMatrix, startStation, targetStations[1])  # ends up at the train station
    if busEndCost < trainEndCost:
        print("The minimum cost path ends up at the bus station (", targetStations[0]+1, "th station ) of the target city.")
        return busEndCost
    else:
        print("The minimum cost path ends up at the train station (", targetStations[1]+1, "th station ) of the target city.")
        return trainEndCost

import random
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1500)

if __name__ == '__main__':

    maxCost = 100
    algoTimes = []
    numOfCityList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in numOfCityList:

        numOfCities = i
        numOfStations = 2*numOfCities
        targetCity = i-1  # 2nd city
        targetStations = [2*(targetCity-1), 2*(targetCity-1)+1]
        startStation = 0  # Bus station in Istanbul
        # startStation = 1  # Train station in Istanbul

        INF = 10000  # used value for cities not connected to each other

        costMatrix = [[random.randint(1, maxCost) for i in range(numOfStations)] for j in range(numOfStations)]

        starttime = time.time()
        print("The Minimum cost to reach", targetCity, "th city is", minCost(costMatrix, startStation, targetStations))
        endtime = time.time()
        algoTime = endtime-starttime
        algoTimes.append(algoTime)


    plt.plot(numOfCityList, algoTimes, linewidth=2.0)
    plt.xlabel('Number of Cities')
    plt.ylabel('runtime Naive Recursion(s)')
    plt.show()
