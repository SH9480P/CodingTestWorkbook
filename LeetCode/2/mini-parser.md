# mini parser

소요시간: 75분

작성일시: 24.06.25 12:50:56

출처: https://leetcode.com/problems/mini-parser/

### 접근 방법
정규표현식으로 정수, \[, \]를 식별 및 순서대로 추출한다.

\[를 만나면 새로운 NestedInteger를 생성하고, \]를 만나면 기존의 NestedInteger에 값을 넣는 것을 중단한다.

재귀호출로 구현할 수도 있었지만, recursion error를 우려하여 stack에 NestedInteger를 저장해두고 top을 참조하여 사용하는 방법을 고안했다.

### 시간 복잡도 분석
O(n)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
인터페이스의 동작을 완전히 파악하지 못하여 시간이 오래 걸렸다.

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
import re
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        p = re.compile(r'-?\d+|[\[\]]')
        arr = p.findall(s)
        listStack = [NestedInteger()]
        for chunk in arr:
            if chunk == '[':
                newNI = NestedInteger()
                listStack[-1].add(newNI)
                listStack.append(newNI)
            elif chunk == ']':
                listStack.pop()
            else:
                chunk = int(chunk)
                listStack[-1].add(NestedInteger(chunk))
        return listStack[0].getList()[0]
```
