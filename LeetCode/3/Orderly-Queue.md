# Orderly Queue

소요시간: NaN

작성일시: 24.05.27 21:53:58

출처: https://leetcode.com/problems/orderly-queue/description/

### 접근 방법
정렬 알고리즘은 swap 연산을 기반으로 작동되는 경우가 많다. 특히, bubble sort는 인접한 두 수를 순차적으로 swap하면서 동작한다.

본 문제의 조건에 따르면, k가 2 이상인 경우, orderly queue의 동작에 의해 인접한 두 수를 swap시킬 수 있다.

위 사실을 알아내었다면, k가 2 이상일 땐 주어진 문자열을 정렬시켜서 반환하고, k가 1일 땐 문자열에 포함된 알파벳 중 lexicographically 제일 작은 문자가 맨 앞에 오는 경우 중 제일 작은 것을 반환할 수 있다.

### 시간 복잡도 분석
O(nlogn)

### 새로 알게 된 것
수열에 포함된 인접한 두 수를 swap할 수 있다면, 전체 수열을 정렬시킬 수 있다. (Bubble Sort)

### 주의할 점
.

### 기타 코멘트
맨 처음 brute force를 생각해 보았으나 경우가 너무 많아질 것 같아 다른 방법을 생각해보았으나, 생각이 나지 않아 결국 다른 사용자의 comment를 읽고 문제를 풀게 되었다.

혼자서 해결하지 못하여 아쉽다.

인접한 두 수를 swap하는 것만으로 수열을 정렬시킬 수 있다는 사실을 알게 되었다는 점에 만족한다.

```python
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            minVal = min(s)
            minStr = chr(123)
            for i in range(len(s)):
                if s[i] == minVal:
                    minStr = min(minStr, s[i:]+s[:i])
            return minStr
        else:
            return ''.join(sorted(s))

s = Solution()
print(s.orderlyQueue('cba', 1))
print(s.orderlyQueue('baaca', 3))
print(s.orderlyQueue('ccbadb', 2))
```
