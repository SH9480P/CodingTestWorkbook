# puyo puyo

소요시간: 90분

작성일시: 24.03.31 20:22:26

출처: https://www.acmicpc.net/problem/11559

### 접근 방법
- 뿌요가 터지면 터진 열에 놓인 뿌요를 아래로 내려야 한다. 이 연산을 쉽게 하기 위해 행과 열을 뒤바꾸어 6X12의 배열을 만들고, 제일 밑의 뿌요는 1열에 놓이도록 했다.
- 같은 색상의 뿌요는 dfs로 찾았다.

### 시간 복잡도 분석
O(12 * 6 * 12 * 12)

### 새로 알게 된 것
.

### 주의할 점
- 동일한 리스트에 대해 원소를 제거하고 추가하는 작업을 여러번 수행하면 기존에 구해놓은 좌표값이 달라질 수 있다. 그래서 뒤에서부터 제거하고 추가해야 한다.

### 기타 코멘트
.

```python
def is_grid_in(x, y):
    return 0 <= x < ROW and 0 <= y < COL

def dfs(x, y, color, dfs_list):
    visited[x][y] = True
    dfs_list.append((x, y))
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if is_grid_in(nx, ny) and not visited[nx][ny] and board[nx][ny] == color:
            dfs(nx, ny, color, dfs_list)

ROW = 6
COL = 12
board = [['.'] * COL for _ in range(ROW)]
for j in range(COL - 1, -1, -1):
    for i, c in enumerate(map(lambda x: x, input())):
        board[i][j] = c

cnt = 0
while True:
    visited = [[False] * COL for _ in range(ROW)]
    explosion = []
    for j in range(COL):
        flag = False
        for i in range(ROW):
            dfs_list = []
            if board[i][j] != '.':
                flag = True
                if not visited[i][j]:
                    dfs(i, j, board[i][j], dfs_list)
            if len(dfs_list) >= 4:
                explosion.extend(dfs_list)
        if not flag:
            break
    if not explosion:
        break
    explosion.sort(key=lambda x: -x[1])
    for ex, ey in explosion:
        board[ex].pop(ey)
        board[ex].append('.')
    cnt += 1

print(cnt)

```
