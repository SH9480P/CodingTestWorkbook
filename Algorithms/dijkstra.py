import heapq

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue

    for node, cost in graph[now]:
        originalDist = distance[node]
        newDist = dist + cost
        if originalDist > newDist:
            distance[node] = newDist
            heapq.heappush(q, (newDist, node))
'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''