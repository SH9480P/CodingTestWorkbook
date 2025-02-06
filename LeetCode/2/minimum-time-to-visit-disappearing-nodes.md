# minimum time to visit disappearing nodes

소요시간: 60분

작성일시: 24.06.26 16:26:24

출처: https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/description/

### 접근 방법
#### 요구사항
- 무방향그래프를 이루는 n개의 node
- edges[i]: [u, v, t] -> u에서 v까지 t의 시간 필요
- disappear[]: 길이 n, i 번째 노드가 사라지는 시간.
- node 0에서 다른 모든 노드까지의 최단 거리를 구해야 함.
- 닿을 수 없으면 -1.
- 노드가 사라지면 노드가 이루는 간선도 같이 사라짐.

#### 문제 분석
- 최장거리는 (5*10**4-1) * 1e5 이므로 INF는 int(5e9)로 한다.
- k초에 사라지는 노드에 k초에 도달하면 도착하지 못한 것으로 간주.
- k초에 사라지는 노드를 k-1초에 도달, 간선을 타고 이동 중에 노드가 사라지면 간선까지 사라지진 않음.
- 무방향 그래프 graph 필요.
- 노드 최단거리 배열 distance 필요.
- 노드 사라지는 시각 배열 disappear 필요.
- 다익스트라 알고리즘의 변형
    - 갱신된 최단거리가 disapper보다 작고 기존 최단거리보다도 작으면 heap 추가
    - 나머지 경우는 continue.

### 시간 복잡도 분석
O(ElogE)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
가능한 조합을 전부 생각해보았다.

기존 최단거리 | 갱신된 최단거리 | disappear
-   1   2   3
    - continue
-   1   3   2
    - continue
-   2   1   3
    - 노드가 사라지기 전 최단거리 발견
    - 갱신
-   2   3   1
    - 기존 최단거리가 disappear보다 크게 설정되는 경우는 존재할 수 없음
    - 고려 X
-   3   1   2
    - 위와 마찬가지
    - 고려 X
-   3   2   1
    - 위와 마찬가지
    - 고려 X
- INF   1   2
    - 노드가 사라지기 전 최초 접근
    - 갱신
- INF   2   1
    - 최초 접근하였으나 노드는 이미 사라지고 난 이후
    - continue

```python
import heapq

class Solution:
    def minimumTime(self, n, edges, disappear):
        INF = int(5e9)
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        distance = [INF] * n
        distance[0] = 0
        q = [(0, 0)]
        while q:
            dist, cur = heapq.heappop(q)
            if dist > distance[cur]:
                continue
            for node, t in graph[cur]:
                newDist = dist + t
                originDist = distance[node]
                if newDist < disappear[node] and newDist < originDist:
                    distance[node] = newDist
                    heapq.heappush(q, (newDist, node))
        return list(map(lambda x: -1 if x == INF else x, distance))
```
