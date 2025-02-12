# insert interval

소요시간: 38분

작성일시: 25.02.09 21:27:30

출처: https://leetcode.com/problems/insert-interval/

### 문제 분석
.

### 접근
- intervals의 원소를 (s1, e1), newInterval를 (s2, e2)라고 할 때,
  - e1 < s2면 순회 continue.
  - e2 < s1이면 순회 break, newInterval 삽입 후 나머지 intervals append.
  - 그 밖의 경우에는 구간이 겹치기 때문에 최소를 start, 최대를 end로 하여 newInterval 갱신

### 유형 분류
.

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
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        for i, interval in enumerate(intervals):
            s1, e1 = interval
            s2, e2 = newInterval
            if e1 < s2:
                answer.append([s1, e1])
            elif e2 < s1:
                answer.append([s2, e2])
                answer.extend(intervals[i:])
                break
            else:
                newInterval = [min(s1, s2), max(e1, e2)]
        else:
            answer.append(newInterval)
        return answer

```