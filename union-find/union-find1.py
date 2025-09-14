def init(n):
    return [i for i in range(n+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[x_root] = y_root
        
n, m = map(int, input().split())
parent = init(n)

for _ in range(m):
    z, x, y = map(int, input().split())
    if z == 1:
        union(parent, x, y)
    else:
        print("Y" if find(parnet, x) == find(parent, y) else "N")