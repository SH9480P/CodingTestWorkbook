# minimum lines to represent a line chart

소요시간: 30분

작성일시: 24.06.20 14:21:27

출처: https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

### 접근 방법
이전 선분의 기울기가 현재 선분의 기울기와 일치하는지 순회하면서 확인, 일치하지 않는 횟수만큼 1 증가하여 반환

### 시간 복잡도 분석
O(nlogn)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x: x[0])
        n = len(stockPrices)
        if n == 1:
            return 0
        dy = (stockPrices[1][1] - stockPrices[0][1])
        dx = (stockPrices[1][0] - stockPrices[0][0])
        answer = 1
        for i in range(2, n):
            ndy = stockPrices[i][1] - stockPrices[i-1][1]
            ndx = stockPrices[i][0] - stockPrices[i-1][0]
            if dy*ndx != dx*ndy:
                dx = ndx
                dy = ndy
                answer += 1
        return answer
```
