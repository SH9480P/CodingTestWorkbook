# append k integers with minimal sum

소요시간: 28분

작성일시: 24.06.21 20:44:36

출처: https://leetcode.com/problems/append-k-integers-with-minimal-sum/

### 접근 방법
합이 최소가 되도록 하려면 sums를 정렬시키고, 앞에서부터 순회하면서 sums에 없는 구간의 자연수를 더해나가면 된다.

문제는 k가 1억개까지 존재할 수 있다는 사실이다. 이를 하나씩 더하면 시간 초과가 우려되는 상황이다.

### 시간 복잡도 분석
O(n)

### 새로 알게 된 것
연속된 자연수를 더해나갈 때, n(n+1)//2를 사용하면 연산을 줄일 수 있다.

### 주의할 점
.

### 기타 코멘트
.

```python
class Solution:
    def sumRange(self, a, b):
        return b*(b+1)//2 - a*(a-1)//2
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0
        prev = 0
        for n in nums:
            if n - prev > 1:
                sub_k = n - prev - 1
                if k - sub_k > 0:
                    answer += self.sumRange(prev+1, n-1)
                    k -= sub_k
                else:
                    answer += self.sumRange(prev+1, prev+k)
                    k = 0
                    break
            prev = n
        if k:
            answer += self.sumRange(nums[-1]+1, nums[-1]+k)
        return answer
```
