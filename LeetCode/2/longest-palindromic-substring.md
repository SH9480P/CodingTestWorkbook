# longest palindromic substring

소요시간: 30분

작성일시: 24.06.18 14:43:28

출처: https://leetcode.com/problems/longest-palindromic-substring/description/

### 접근 방법
최초 brute force를 생각했으나 시간초과가 예상되어 DP로 접근할 수 있는지 알아보았다.

Palindrome인 Substring의 양 옆에 동일한 문자를 붙여 palindrome을 만들 수 있다.

s[k:k+1]은 당연히 palindrome이고, s[k:k+2] 중에 동일한 문자가 2번 반복되면 palindrome이다.

위 초기 palindrome substrings를 대상으로 양 옆에 동일한 문자가 오는지 확인, 온다면 palindrome이므로 다시 동일한 문자가 오는지 확인하는 작업을 반복한다.

### 시간 복잡도 분석
O(n^2)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = deque((i,i) for i in range(n))
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp.append((i, i + 1))
        while dp:
            i, j = dp.popleft()
            if i - 1 >= 0 and j + 1 < n and s[i-1] == s[j+1]:
                dp.append((i-1, j+1))
            elif not dp:
                return s[i:j+1]
```
