# find subarray with bitwise and closest to k

소요시간: NaN

작성일시: 24.06.02 23:54:05

출처: https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/

### 접근 방법
##### 1st
.

##### 2nd
.

### 시간 복잡도 분석
.

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
class Solution:
    def minimumDifference(self, nums, k) -> int:
        min_diff = int(1e9)
        n = len(nums)
        for i in range(n):
            sub_result = -1
            for j in range(i, n):
                sub_result &= nums[j]
                min_diff = min(min_diff, abs(sub_result - k))
                if sub_result < k:
                    break
                if sub_result == k:
                    return 0
        return min_diff
```
