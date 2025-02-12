# merge intervals

소요시간: 10분

작성일시: 25.02.09 20:23:59

출처: https://leetcode.com/problems/merge-intervals/

### 문제 분석
- 겹치는 튜플을 하나로 만들기
- 튜플은 1개 이상 1만개 이하 제공.

### 접근
- 튜플 정렬
- prev.end와 cur.start를 비교
    - cur.start <= prev.end 이면 튜플 합치기

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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        answer = [intervals[0]]
        for cur in intervals[1:]:
            prev = answer[-1]
            if cur[0] <= prev[1]:
                answer.pop()
                answer.append([prev[0], max(prev[1], cur[1])])
            else:
                answer.append(cur)
        return answer

```