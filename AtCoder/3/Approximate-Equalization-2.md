## Approximate Equalization 2

출처: https://atcoder.jp/contests/abc313/tasks/abc313_c

수열의 길이 = N
시간복잡도 = O(NlogN)

### Idea

- 연산 수행 전후 수열의 합은 항상 동일
- 두 수열의 합이 동일하다면 연산을 수행하여 두 수열을 같게 만들 수 있음
- 두 수열을 같게 만들기 위한 연산의 최소 횟수는 다음과 같은 방법으로 구할 수 있음
  - 서로 다른 두 수열의 같은 index에 위치한 수 끼리의 차를 모두 더하면 +k - k가 나오는데, 여기서 k가 연산의 최소 횟수  
   == 서로 다른 두 수열의 같은 index에 위치한 수 끼리의 차에 절댓값을 취한 값을 모두 더하여 2로 나누기
- 주어진 수열의 평균을 구하면 n.xxxx가 나올 것임. 즉, 연산을 반복한 결과로 보아야 하는 수열은 n과 n+1로만 이루어진 수열이며, n+1의 수는 수열의 합을 길이로 나눈 나머지.
- 최초 수열과 마지막 수열을 모두 정렬시킨 뒤에 연산의 최소 횟수를 구하면 됨 (마지막 수열의 정렬 형태에 따라 다양한 값이 나오며, 최솟값을 취하려면 같은 위치의 수 간 차이의 절댓값이 작아야 하기 때문)

### 아쉬웠던 점

- 접근법 자체를 못 찾음
```python
N = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
s = sum(arr)
q = s // N
r = s % N

final = [q] * N
for i in range(r):
    final[i] += 1

result = 0
for i in range(N):
    result += abs(arr[i] - final[i])

print(result // 2)
```
