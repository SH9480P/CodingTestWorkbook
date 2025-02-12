# fence planning

소요시간: 50분

작성일시: 25.02.12 19:22:09

출처: https://www.acmicpc.net/problem/17197

### 문제 분석
- 소 마릿수: 2 이상 10만 이하
- 간선 수: 1 이상 10만 이하
- 소 좌표: 0 이상 10^8 이하
- 네트워크 하나가 온전히 포함되게 펜스를 친다. 단, 둘레가 최소가 되어야 한다.

### 접근
- union find로 네트워크 식별
- 단일 네트워크에서 x, y 좌표의 최대, 최소 구하기
- 둘레 최소 구하기

### 유형 분류
- union-find

### 시간 복잡도 분석
O(N)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

### 코드
```python
import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
situated = [(0, 0)]
for _ in range(N):
    a, b = map(int, input().split())
    situated.append((a, b))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    if a < b:
        graph[a].append(b)
    else:
        graph[b].append(a)
parent = list(range(N+1))

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

def seperateByNetwork():
    for i in range(1, N+1):
        for j in graph[i]:
            union(i, j)
    for i in range(1, N+1):
        find(i)
    networkDict = {}
    for i in range(1, N+1):
        if parent[i] in networkDict:
            networkDict[parent[i]].append(i)
        else:
            networkDict[parent[i]] = [i]
    return list(networkDict.values())

def getMinPerimeter(groups):
    INF = int(1e9)
    minVal = INF
    for group in groups:
        minX, minY, maxX, maxY = INF, INF, 0, 0
        for id in group:
            x, y = situated[id]
            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, x)
            maxY = max(maxY, y)
        perimeter = (maxX - minX + maxY - minY) * 2
        minVal = min(minVal, perimeter)
    return minVal

groups = seperateByNetwork()
perimeter = getMinPerimeter(groups)
print(perimeter)

```