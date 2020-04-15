
def shortestPathFinder(graph, path, stationNum, start, destinations):

    for k in range(stationNum):  # pick all city station as source one by one
        for i in range(stationNum):  # pick all city stations as destination for the kth city
            for j in range(stationNum):  # If city station k is on the shortest path from i to j then update dist[i][j]
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    # if the city station is the shortest path from i to j update cost and path
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j] = path[k][i]

    print("\nShortest itinerary from Istanbul bus station to nth city costs:")

    if graph[start][destinations[0]] <= graph[start][destinations[1]]:  # Ends up at the Bus station
        destination = destinations[0]
        printSolution(graph, path, stationNum, start, destination)
        return graph[start][destinations[0]]
    else:                                                               # Ends up at the Train station
        destination = destinations[1]
        printSolution(graph, path, stationNum, start, destination)
        return graph[start][destinations[1]]

def printPath(path, v, u):
    if path[v][u] != v:
        printPath(path, v, path[v][u])
    print(path[v][u], "->")

# printing the final solution of cost table
def printSolution(dist, path, stationNum, start, destination):
    print("Matrix for the shortest distances between pair of stations:")
    for i in range(stationNum):
        str = ""
        for j in range(stationNum):
            if dist[i][j] == INF:
                str += ("%5s" % "INF")
            else:
                str += ("%5d\t" % (dist[i][j]))
            if j == stationNum - 1:
                str += ""
        print(str)
    print("Path to", destination//2, "from Istanbul:")
    printPath(path, start, destination)
    print("=>", destination)


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

import sys
sys.setrecursionlimit(4000)

if __name__ == '__main__':

    numOfCities = 5
    numOfStations = 2*numOfCities
    targetCity = 5  # 5th city
    targetStations = [2*(targetCity-1), 2*(targetCity-1)+1]
    startStation = 0  # Bus station in Istanbul
    # startStation = 1  # Train station in Istanbul

    INF = 10000  # used value for cities not connected to each other

    costMatrix = [[  0,   1,   8, INF,  16, INF,  25, INF,  20, INF],
                  [  1,   0, INF,   2, INF,  14, INF,  20, INF,  17],
                  [  8, INF,   0,   2,   4, INF,  12, INF, INF, INF],
                  [INF,   2,   2,   0, INF, INF, INF,  10, INF, INF],
                  [ 16, INF,   4, INF,   0,   1,   7, INF,  13, INF],
                  [INF,  14, INF, INF,   1,   0, INF,   3, INF,  10],
                  [ 25, INF,  12, INF,   7, INF,   0,   1,   2, INF],
                  [INF,  20, INF,  10, INF,   3,   1,   0, INF, INF],
                  [ 20, INF, INF, INF,  13, INF,   2, INF,   0,   3],
                  [INF,  17, INF, INF, INF,  10, INF, INF,   3,   0],
                  ]

    path = [[INF for i in range(numOfStations)] for j in range(numOfStations)]
    for i in range(numOfStations):
        strr = ""
        for j in range(numOfStations):
            if i == j:
                path[i][j] = 0
            elif costMatrix[i][j] != INF:
                path[i][j] = i
            else:
                path[i][j] = -1

    print("(Naive Recursion)The Minimum cost to reach", targetCity, "th city is", minCost(costMatrix, startStation, targetStations))

    print("(DP-Memoization)Total minimum cost:", shortestPathFinder(costMatrix, path, numOfStations, startStation, targetStations))

