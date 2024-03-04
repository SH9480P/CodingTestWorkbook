def solution(graph, start):
    INF = int(1e9)
    N = len(graph)
    distance = [INF] * N
    distance[start] = 0

    for _ in range(N - 1):
        for i in range(N):
            for node, weight in graph[i]:
                originalDist = distance[node]
                newDist = distance[i] + weight
                if originalDist > newDist:
                    distance[node] = newDist

    for i in range(N):
        for node, weight in graph[i]:
            originalDist = distance[node]
            newDist = distance[i] + weight
            if originalDist > newDist:
                return [-1]
    return distance

print(solution([[(1,4), (2,3), (4,-6)], [(3,5)], [(1,2)], [(0,7), (2,4)], [(2,2)]], 0))