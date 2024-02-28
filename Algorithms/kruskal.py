'''
# 최소 신장 트리 찾기
1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    사이클이 발생하지 않으면 최소 신장 트리에 포함시킨다.
    사이클이 발생하면 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대해 2번을 수행한다.

# input
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''

def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = list(range(v+1))

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

totalCost = 0
for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        totalCost += cost

print(totalCost)