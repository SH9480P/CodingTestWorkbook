'''
# 위상 정렬
1. 진입 차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다
    새롭게 진입 차수가 0이 된 노드를 큐에 넣는다

# input
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''
from collections import deque

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)

answer = []
while q:
    cur = q.popleft()
    answer.append(cur)
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(answer)