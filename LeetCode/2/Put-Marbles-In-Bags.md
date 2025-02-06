# Put Marbles In Bags

소요시간: 65분

작성일시: 24.05.26 18:50:26

출처: https://leetcode.com/problems/put-marbles-in-bags/description/

### 접근 방법
먼저 Brute Force 방법을 고려해보았다.

수열을 분할한다고 생각하면, 분할의 기준이 되는 수를 고름으로써 전체 경우의 수를 구할 수 있다. 즉, 구슬 수를 n이라 할 때, n-1개의 구슬 중 k-1개를 뽑는 조합을 구하여 최댓값과 최솟값을 계산하면 된다.

문제는 n의 범위가 최대 10000까지라는 것이다. 따져 봐야 할 경우가 너무 많아 실행 시간이 길어질 것이다.

 

다음으로 Greedy하게 해결할 수 있을지 고민해보았다.

맨 처음 구슬과 맨 나중 구슬의 weight는 가방의 cost에 반드시 포함되므로 무시해도 좋다.

맨 처음과 나중의 구슬은 무시하면 partition의 경계를 이루는 구슬을 2개씩 짝지을 수 있다.

전체 cost는 partition을 이루는 2개의 구슬 짝을 모두 더한 값이 된다.

최댓값을 구하려면, 구슬 짝의 합이 제일 큰 것들만 고르면 되고, 최솟값을 구하려면 구슬 짝의 합이 제일 작은 것들만 고르면 된다.

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
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_sum_arr = []
        n = len(weights)
        for i in range(n-1):
            pair_sum_arr.append(weights[i] + weights[i+1])
        pair_sum_arr.sort()
        return sum(pair_sum_arr[n-k:n-1]) - sum(pair_sum_arr[:k-1])
```
