# Got the initial code from: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
# It is basically, Floyd-Warshall Algorithm with path recording

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


if __name__ == '__main__':

    numOfCities = 3
    numOfStations = 2*numOfCities
    targetCity = 3  # 3rd city / last city
    targetStations = [2*(targetCity-1), 2*(targetCity-1)+1]
    startStation = 0  # Bus station in Istanbul
    # startStation = 1  # Train station in Istanbul

    INF = 10000  # used value for cities not connected to each other

                # ______________________________
                # | First   | Second  | Third  |  City
                # | 0b   0t | 1b   1t | 2b   2t|
    costMatrix = [[  0,   2,   6, INF,   2, INF],
                  [  2,   0, INF,   5, INF,   4],  #0t
                  [  6, INF,   0,   3,   3, INF],  #1b
                  [INF,   5,   3,   0,   3,   1],  #1t
                  [2  , INF,   3, INF,   0,   1],  #2b
                  [INF, 4  , INF,   1,   1,   0],  #2t
                 ]

    print("Initial paths:")
    path = [[INF for i in range(numOfStations)] for j in range(numOfStations)]
    print(path)

    for i in range(numOfStations):
        strr = ""
        for j in range(numOfStations):
            if i == j:
                path[i][j] = 0
            elif costMatrix[i][j] != INF:
                path[i][j] = i
            else:
                path[i][j] = -1

    print("\nChanged paths:")
    for i in range(numOfStations):
        strr = ""
        for j in range(numOfStations):
            strr += (str(path[i][j]) + " ")
        print(strr)

    print("Total minimum cost:", shortestPathFinder(costMatrix, path, numOfStations, startStation, targetStations))

