# A → B

소요시간: 16분

작성일시: 25.02.18 20:57:30

출처: https://www.acmicpc.net/problem/16953

### 문제 분석
- A는 1 이상, B는 A보다 크거나 같고, B는 1e9보다 작음
- 2가지 연산을 수행할 수 있을 때, A와 B가 같아지기까지 연산의 최솟값 + 1을 구하라.
- A와 B가 같아질 수 없다면 -1 출력.

### 접근
- B에서 A를 만들 수 있는지 구하자.
- B가 짝수면 2로 나누고, 1로 끝나면 1을 떼버리자.

### 유형 분류
- 그리디

### 시간 복잡도 분석
- log(B)

### 새로 알게 된 것
.

### 주의할 점
- A가 B보다 커지는 경우를 고려하지 않으면 무한루프가 발생한다.

### 기타 코멘트
.

### 코드
```python
a, b = map(int, input().split())

cnt = 1
while True:
    if a == b:
        break
    if a > b:
        cnt = -1
        break
    last = b % 10
    if last % 2 == 0:
        b //= 2
        cnt += 1
    elif last == 1:
        b //= 10
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)
```