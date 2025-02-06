# capacity to ship packages within d days

소요시간: 70분

작성일시: 24.06.12 00:02:19

출처: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

### 접근 방법
부분수열의 합의 최댓값을 binary search로 탐색하는 방법.

### 시간 복잡도 분석
N = weights 길이, S = weights 합

O(NlogS)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weight = sum(weights)
        max_weight = max(weights)
        left = max(total_weight // days, max_weight)
        right = total_weight
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            d = 0
            sub_weights = 0
            for i in range(len(weights)):
                if sub_weights + weights[i] < mid:
                    sub_weights += weights[i]
                elif sub_weights + weights[i] > mid:
                    sub_weights = weights[i]
                    d += 1
                else:
                    sub_weights = 0
                    d += 1
            if sub_weights:
                d += 1
            if d <= days:
                right = mid - 1
                answer = mid
            else:
                left = mid + 1
        return answer
                
```
