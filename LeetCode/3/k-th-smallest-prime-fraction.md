# k th smallest prime fraction

소요시간: NaN

작성일시: 24.06.11 17:37:29

출처: https://leetcode.com/problems/k-th-smallest-prime-fraction/description/

### 접근 방법
가능한 모든 경우를 나열하여 정렬시키고 kth 분수를 반환하면 너무 오래 걸릴 것이다.

1~k th의 분수만 구하는 것이 좋겠다.

제일 작은 값은 arr[0]/arr[-1] 이다.

그 다음으로 작은 값은 arr[1] / arr[-1] 또는 arr[0] / arr[-2]가 될 것이다.

무엇이 더 작은지 비교하는 것은 min-heap에 맡기자.

arr[i] / arr[j]는 arr[i] / arr[j-1]보다 항상 작기 때문에, arr[i]/arr[j]를 pop하면 arr[i]/arr[j-1]를 넣을 수 있다.

heap에서 k번 pop하면 분수를 구할 수 있다.

### 시간 복잡도 분석
O(NlogN)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        q = []
        n = len(arr)
        for i in range(n-1):
            heapq.heappush(q, (arr[i]/arr[-1], i, n-1))
        a, b = 0, 0
        for _ in range(k):
            _, i, j = heapq.heappop(q)
            a, b = arr[i], arr[j]
            if j-1 > i:
                heapq.heappush(q, (arr[i]/arr[j-1], i, j-1))
        return [a, b]
        
```
