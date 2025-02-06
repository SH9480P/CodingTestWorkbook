# milk scheduling

소요시간: 45분

작성일시: 24.05.19 17:34:39

출처: https://www.acmicpc.net/problem/9869

참고: https://youtu.be/x9iDSJHV8F8?si=xTuJH-L1_hdhjaSZ

### 접근 방법
마감 기한이 있는 스케줄링

2nd  
제일 가치가 높은 작업부터 선택하되, 선택한 작업을 포함하여 유효한 스케줄을 생성할 수 없으면 선택하지 않고 다음 작업을 선택한다.  
선택 가능한 작업의 마감 기한을 유효한 순서대로 저장해둘 때, 마감 기한이 큰 값부터 조회하면(뒤에서부터 비교해나가면) 비교 연산을 줄일 수 있다.

3rd  
유효한 스케줄 중 제일 가치가 높은 작업을 많이 포함하는 스케줄을 골라야 하므로, 먼저 유효한 스케줄을 만들고 그 다음에 가치 계산을 수행해보자.  
마감 기한이 제일 늦은 작업부터 살펴본다. 현재의 마감 기한을 앞으로 선택할 수 있는 작업의 수로 여기면 유효한 스케줄을 만들 수 있다.  
문제가 되는 부분은 동일한 마감 기한이 여러 번 등장했을 때, 앞으로 살펴볼 이른 마감 기한의 작업의 가치와 현재 살펴보고 있는 동일한 마감 기한의 작업들의 가치 중 어느 것이 더 높은지 알 수 없다는 것이다.  
이 부분은 우선순위 큐를 도입하여 해결할 수 있다. 마감 기한이 같은 작업들의 가치를 모두 우선순위 큐에 넣고, 제일 높은 가치의 작업을 선택한다. 다음으로 마감 기한이 이른 작업을 살펴볼 땐, 우선순위 큐에서 빠져나가지 못한 늦은 마감 기한의 작업의 가치와 함께 비교하여 더 높은 가치의 작업을 선택하는 과정을 거쳐 스케줄의 유효성과 최대 가치를 지킬 수 있다.

### 시간 복잡도 분석
2nd: O(n^2)  
3rd: O(nlogn)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
2nd 방법은 유튜브 영상을 보고, 3rd 방법은 백준에서 다른 사람의 풀이를 보고 알게 되었다.  
이와 같은 문제를 처음 만났다고 가정했을 때 접근법을 생각해보자.  
이 문제에서 다루어야 하는 데이터는 작업의 마감 기한과 작업의 가치이다. 마감 기한을 어기지 않도록 작업을 선택하되, 작업의 총 가치를 최대로 해야 한다.  
작업의 가치를 내림차순으로 정렬시키고, 가치가 큰 작업부터 차례대로 살펴보면서 마감 기한이 지켜지는지 검사하고, 지켜지면 스케줄에 포함하는 식으로 접근할 수 있다.  
마감 기한을 내림차순으로 정렬시키고, 마감 기한이 제일 늦은 작업부터 차례대로 살펴보면서, 마감 기한이 동일한 작업이 여러 개 등장하면 그 중에서 제일 가치가 높은 작업을 먼저 선택하는 식으로 접근할 수도 있다.  
이걸 어떻게 생각해내냐 어렵네 정말

```python
import sys

input = sys.stdin.readline

N = int(input())
gd = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
gd.sort(key=lambda x: x[0], reverse=True)

schedule = [0]
total = 0
for i in range(N):
    milk, deadline = gd[i]
    inserted_idx = len(schedule)
    for j in range(len(schedule)):
        if deadline < schedule[j]:
            inserted_idx = j
            break
    if inserted_idx > deadline:
        continue
    for j in range(inserted_idx, len(schedule)):
        if j + 1 > schedule[j]:
            break
    else:
        schedule.insert(inserted_idx, deadline)
        total += milk
print(total)
```
```python
import sys

input = sys.stdin.readline

N = int(input())
gd = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
gd.sort(key=lambda x: x[0], reverse=True)

schedule = [0]
total = 0
for i in range(N):
    milk, deadline = gd[i]
    for j in range(len(schedule)-1, -1, -1):
        if schedule[j] > deadline:
            if j + 1 > schedule[j]:
                break
        elif j + 1 > deadline:
            break
        else:
            schedule.insert(j+1, deadline)
            total += milk
            break
print(total)
```
```python
import heapq
import sys

def solution(N, cows):
    cows.sort(key=lambda x: x[1], reverse=True)
    tickets = cows[0][1]
    i = 0
    candidates = []
    answer = 0
    while i < N:
        g, d = cows[i]
        if d == tickets:
            heapq.heappush(candidates, -g)
            i += 1
        elif d < tickets:
            if candidates:
                answer -= heapq.heappop(candidates)
                tickets -= 1
            else:
                tickets = d
    for _ in range(min(tickets, len(candidates))):
        answer -= heapq.heappop(candidates)
    return answer

input = sys.stdin.readline
N = int(input())
cows = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(N, cows))
```
