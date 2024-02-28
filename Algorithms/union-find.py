# input
## 6 4
## 1 4
## 2 3
## 2 4
## 5 6

# 유의사항
## 경로 압축 기법을 사용하여 find 연산의 호출 횟수를 줄였음
## 그러나 모든 최종 parent가 저장되어있는 것은 아니므로, 마지막에 전체 노드에 대해 find 연산을 한 번씩 더 수행해야 함

def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = list(range(v+1))

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(a, b)
    
for i in range(1, v+1):
    find_parent(i)
print(parent[1:])
