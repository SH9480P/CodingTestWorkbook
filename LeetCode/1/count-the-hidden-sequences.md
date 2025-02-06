# count the hidden sequences

소요시간: 20분

작성일시: 24.06.16 23:56:15

출처: https://leetcode.com/problems/count-the-hidden-sequences/

### 접근 방법
.

### 시간 복잡도 분석
O(n)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        arr = [0]
        for i in range(len(differences)):
            arr.append(arr[i] + differences[i])
        max_val = max(arr)
        min_val = min(arr)

        val = (upper - max_val) - (lower - min_val) + 1
        return val if val > 0 else 0
```
