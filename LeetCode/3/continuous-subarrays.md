# continuous subarrays

소요시간: NaN

작성일시: 24.06.24 10:56:01

출처: https://leetcode.com/problems/continuous-subarrays/description/

### 접근 방법
sub array는 연속되어야 한다.

sub array의 right를 기준으로, right가 0에서 n-1이 되는 경우에 대해 sub array를 찾아나간다.

right - 1, right - 2, ... 를 순차적으로 조회하면서 sub array에 포함시킬지 확인할 수 있다. 

하지만 위 방법은 O(n^2)의 시간복잡도를 보이며, 시간초과가 우려된다.

연속된 집합의 최솟값과 최댓값을 알 수 있다면, 해당 값이 sub array에 포함되지 않는 경우 중 제일 오른쪽에 위치하는 값이 현재 sub array의 바로 왼쪽 값이 될 것이다.

최댓값과 최솟값을 조회하는 작업은 heap을 사용한다.

### 시간 복잡도 분석
O(nlogn)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
import heapq

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        max_q, min_q = [], []
        left = -1
        for right in range(n):
            while max_q and -max_q[0][0] - nums[right] > 2:
                left = max(left, heapq.heappop(max_q)[1])
            while min_q and min_q[0][0] - nums[right] < -2:
                left = max(left, heapq.heappop(min_q)[1])
            heapq.heappush(max_q, (-nums[right], right))
            heapq.heappush(min_q, (nums[right], right))
            answer += right - left
        return answer
        
```
