# N Queen

소요시간: NaN

작성일시: 24.03.06 10:46:48

출처: https://school.programmers.co.kr/learn/courses/30/lessons/12952

### 접근 방법
1st
- backtracking.
- 시간 초과

2nd
- 퀸을 놓을 수 있는지 검사할 때, 세로 방향과 두 대각선 방향에 이미 놓인 퀸이 있는지 기록하는 배열을 만들어 사용함으로써 실행 시간을 줄일 수 있었다.

### 시간 복잡도 분석
O(N!)

### 새로 알게 된 것
.

### 주의할 점
.

### 기타 코멘트
.

```python
def solution(n):
    board = [[False] * n for _ in range(n)]

    def isGridIn(r, c):
        return 0 <= r < n and 0 <= c < n

    def isSafe(r, c):
        for i in range(n):
            if board[i][c]:
                return False
        i, j = r-1, c-1
        while isGridIn(i, j):
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        i, j = r-1, c+1
        while isGridIn(i, j):
            if board[i][j]:
                return False
            i -= 1
            j += 1
        return True

    def put(board, row):
        if row == n:
            return 1
        result = 0
        for i in range(n):
            if isSafe(row, i):
                board[row][i] = True
                result += put(board, row + 1)
                board[row][i] = False
        return result

    return put(board, 0)
```
```python
def solution(n):
    board = [[False] * n for _ in range(n)]
    columnCheck = [False] * n
    rightUpDiagonalCheck = [False] * (2 * n - 1)
    leftUpDiagonalCheck = [False] * (2 * n - 1)

    def isSafe(r, c):
        return not columnCheck[c] and not rightUpDiagonalCheck[r-c+n-1] and not leftUpDiagonalCheck[r+c]

    def mark(row, col, value: bool):
        board[row][col] = value
        columnCheck[col] = value
        rightUpDiagonalCheck[row - col + n - 1] = value
        leftUpDiagonalCheck[row + col] = value

    def put(board, row):
        if row == n:
            return 1
        result = 0
        for i in range(n):
            if isSafe(row, i):
                mark(row, i, True)
                result += put(board, row + 1)
                mark(row, i, False)
        return result

    return put(board, 0)
```
