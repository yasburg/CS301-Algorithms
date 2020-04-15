# Python program to find min cost path
# from station 0 to station N-1
import sys
sys.setrecursionlimit(1500)

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

if __name__ == '__main__':

    numOfCities = 3
    numOfStations = 2*numOfCities
    targetCity = 3  # 3rd city
    targetStations = [2*(targetCity-1), 2*(targetCity-1)+1]
    startStation = 0  # Bus station in Istanbul
    # startStation = 1  # Train station in Istanbul

    INF = 10000  # used value for cities not connected to each other

                # ______________________________
                # | First   | Second  | Third  |  City
                # | 0b   0t | 1b   1t | 2b   2t|
    costMatrix = [[  0,   2,   6, INF, INF, INF],
                  [  2,   0, INF,   5, INF,   4],  #0t
                  [  6, INF,   0,   3,   3, INF],  #1b
                  [INF,   5,   3,   0,   3,   1],  #1t
                  [INF, INF,   3, INF,   0,   1],  #2b
                  [INF, 4  , INF,   1,   1,   0],  #2t
                 ]
    """
    Black-box testing 1: Works!
    costEmpty = [[]]  # targetCity = 0

    Black-box testing 2: Works!
    costEmpty = [[0], [1]]  # targetCity = 1
  
    Black-box testing 3: Works (tested in analysis.py file)!
  
    Black-box testing 4: Works!
    cost0s = [  [ 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0],  #0t
                [ 0, 0, 0, 0, 0, 0],  #1b
                [ 0, 0, 0, 0, 0, 0],  #1t
                [ 0, 0, 0, 0, 0, 0],  #2b
                [ 0, 0, 0, 0, 0, 0]  #2t
                 ]
                 
    Black-box testing 5: Works!
    costINFs = [[ INF, INF, INF, INF, INF, INF],
                [ INF, INF, INF, INF, INF, INF],
                [ INF, INF, INF, INF, INF, INF],
                [ INF, INF, INF, INF, INF, INF],
                [ INF, INF, INF, INF, INF, INF],
                [ INF, INF, INF, INF, INF, INF]
                ]
    """

    print("The Minimum cost to reach", targetCity, "th city is", minCost(costMatrix, startStation, targetStations))

