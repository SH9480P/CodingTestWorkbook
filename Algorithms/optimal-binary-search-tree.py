def opt_bst():
    n = len(p) - 1
    A = [[-1] * (n+1) for _ in range(n+2)]
    R = [[-1] * (n+1) for _ in range(n+2)]
    for i in range(1, n+1):
        A[i][i] = p[i]
        A[i][i-1] = 0
        R[i][i] = i
        R[i][i-1] = 0
    A[n+1][n] = 0
    R[n+1][n] = 0

    for diff in range(1, n):
        for i in range(1, n - diff + 1):
            j = i + diff
            min_val = int(1e9)
            min_k = int(1e9)
            for k in range(i, j+1):
                val = A[i][k-1] + A[k+1][j]
                if val < min_val:
                    min_val = val
                    min_k = k
            A[i][j] = min_val + sum(p[i:j+1])
            R[i][j] = min_k
    return A, R

def print_preorder_opt_bst(R, start, end):
    if start > end:
        return
    root_idx = R[start][end]
    print(keys[root_idx], end=' ')
    print_preorder_opt_bst(R, start, root_idx-1)
    print_preorder_opt_bst(R, root_idx+1, end)



keys = list(range(0, 60, 10))
p = [0, 35, 12, 22, 8, 15]

A, R = opt_bst()
opt_search_cost = A[1][len(p)-1]
print(opt_search_cost)
print_preorder_opt_bst(R, 1, len(p)-1)
