# 2xn 타일링

소요시간: 7분

작성일시: 24.03.22 21:54:48

출처: https://school.programmers.co.kr/learn/courses/30/lessons/12900

### 접근 방법
dp

### 시간 복잡도 분석
O(n)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
def solution(n):
    if n == 1:
        return 1
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[-1] % 1000000007
```
