# H index 2

소요시간: 35분

작성일시: 24.06.14 11:43:26

출처: https://leetcode.com/problems/h-index-ii/description/

### 접근 방법
citations는 정렬되어있다.

현재 idx를 포함하여 뒤로 남아있는 citation의 개수가 현재 idx의 citation값보다 작으면 H-index로 삼을 수 있다.

위의 조건에 맞는 idx를 찾는 과정은 순차 탐색으로도 가능하고, 이분 탐색으로도 가능하다.

### 시간 복잡도 분석
O(logN)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
leetcode 상에서는 두 solutions의 실행 시간에 차이가 없다.

테스트케이스가 편향되어있는 것일까?

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for i in range(n):
            if n-i <= citations[i]:
                return n-i
        return 0
        
```
```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n-1
        while left <= right:
            mid = (left+right)//2
            if n - mid < citations[mid]:
                right = mid - 1
            elif n - mid > citations[mid]:
                left = mid + 1
            else:
                return n - mid
        return n - left if left < n else 0
```
