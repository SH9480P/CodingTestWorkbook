# minimum number of coins for fruits

소요시간: 2시간

작성일시: 24.06.23 14:29:37

출처: https://leetcode.com/problems/minimum-number-of-coins-for-fruits/description/

### 접근 방법
##### 점화식
DP[i][0]: i th 과일의 값을 지불하지 않고 i번째까지의 최소 구매 비용

DP[i][1]: i th 과일의 값을 지불한 상태에서 i번째까지의 최소 구매 비용

DP[i][1] = min(DP[i-1][0], DP[i-1][1]) + prices[i]  
k가 i+1 ~ 2i+1일 때, DP[k][0] = min(DP[k][0], DP[i][1])

### 시간 복잡도 분석
O(N^2)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return prices[0]
        INF = int(1e9)
        d = [[INF]*2 for _ in range(n)]
        d[0][1] = prices[0]
        d[1][0] = prices[0]
        for i in range(1, n):
            d[i][1] = min(d[i-1]) + prices[i]
            for j in range(i+1, min(2*i+2, n)):
                d[j][0] = min(d[i][1], d[j][0])
        return min(d[-1])
```
