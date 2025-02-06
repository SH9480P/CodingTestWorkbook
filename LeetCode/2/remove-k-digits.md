# remove k digits

소요시간: 90분

작성일시: 24.06.20 11:16:22

출처: https://leetcode.com/problems/remove-k-digits/

### 접근 방법
ith index를 기준으로 i-1 th index의 값이 더 크면 i-1을 삭제한다.

k만큼 위의 과정을 반복하되, k만큼 삭제하기 전에 전체 문자열을 순회했다면 문자열은 증가하는 양상을 보일 것이기 때문에 맨 뒤에서부터 남은 삭제 횟수만큼 삭제한다.

### 시간 복잡도 분석
O(n)

### 새로 알게 된 것
.

### 주의할 점
테스트케이스를 많이 만들어두자.

### 기타 코멘트
.

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n <= k:
            return "0"
        answer = [num[0]]
        i = 1
        deleted = 0
        while i < n:
            if deleted == k:
                last = num[i:]
                j = 0
                if not answer:
                    while j < len(last):
                        if last[j] != '0':
                            break
                        j += 1
                answer.extend(list(last[j:]))
                break
            if answer and answer[-1] > num[i]:
                answer.pop()
                deleted += 1
            else:
                if answer or num[i] != '0':
                    answer.append(num[i])
                i += 1
        if not answer:
            return '0'
        elif deleted < k:
            if len(answer) <= k-deleted:
                return '0'
            else:
                return ''.join(answer[:len(answer)-(k-deleted)])
        else:
            return ''.join(answer)
```
