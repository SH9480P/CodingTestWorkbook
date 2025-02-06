# maximum number of alloys

소요시간: 110분

작성일시: 24.06.16 15:50:26

출처: https://leetcode.com/problems/maximum-number-of-alloys/

### 접근 방법
n은 금속 가짓수, k는 기계 수량

x, y, z가 각 금속을 구입하는데 사용한 coin이고, cost를 a, b, c라고 할 때, composition을 p, q, r이라고 할 때,  
x >= pak - a*stock(x)  
y >= qbk - b*stock(y)  
z >= rck - c*stock(z)  
x+y+z <= budget

위 식을 만족하는 k값 중 최댓값을 골라야 함.

k값을 binary search로 탐색하면서 최댓값을 찾을 수 있을까?

### 시간 복잡도 분석
O(logn)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        max_val = 0
        for i in range(k):
            comp = composition[i]
            max_val = max(self.bs(n, k, budget, comp, stock, cost), max_val)
        return max_val

    def bs(self, n, k, budget, comp, stock, cost):
        left = 1
        right = (budget + sum(map(lambda x: cost[x]*stock[x], range(n)))) // sum(map(lambda x: cost[x]*comp[x], range(n)))
        while left <= right:
            mid = (left + right) // 2
            paid = [0]*n
            for i in range(n):
                paid[i] = max(comp[i]*cost[i]*mid - stock[i]*cost[i], 0)
            if sum(paid) <= budget:
                left = mid + 1
            else:
                right = mid - 1
        return right
```
