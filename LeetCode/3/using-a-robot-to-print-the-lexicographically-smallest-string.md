# using a robot to print the lexicographically smallest string

소요시간: NaN

작성일시: 24.06.25 10:28:11

출처: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/

### 접근 방법
그리디한 접근법이 존재한다.

t 스택의 top과 남은 문자열 중 제일 작은 문자를 비교, 제일 작은 문자가 남은 문자열에 존재하면 t에 push, 그렇지 않으면 t의 top을 pop한다.

### 시간 복잡도 분석
O(26n)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
접근법이 보이지 않았다.

문제를 단순하게, 크게 보자.

```python
from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        answer = ''
        t = []
        i = 0
        while i < len(s):
            minChar = self.minCharLeft(counter)
            if not t or t[-1] > minChar:
                t.append(s[i])
                counter[s[i]] -= 1
                i += 1
            else:
                answer += t.pop()
        if t:
            answer += ''.join(t[::-1])
        return answer

    def minCharLeft(self, counter):
        for char in map(lambda x: chr(x), range(ord('a'), ord('z')+1)):
            if counter[char] > 0:
                return char
        return 'zz'
    
```
