# N으로 표현

소요시간: NaN

작성일시: 24.03.23 20:42:41

출처: https://school.programmers.co.kr/learn/courses/30/lessons/42895

### 접근 방법
N을 사용한 횟수에 따른 결과값을 dp table에 저장하면 8회까지 차례대로 구할 수 있음.

### 시간 복잡도 분석
.

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
def solution(N, number):
    if number == N:
        return 1
    dp = [set(), {N}]
    for i in range(2, 9):
        dp.append({int(str(N)*i)})
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].update([a+b, a-b, a*b])
                    if b != 0:
                        dp[i].add(a//b)
        if number in dp[i]:
            return i
    return -1
```
