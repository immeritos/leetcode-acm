import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent):
    has_red = has_black = False
    if colors[node] == 'R':
        has_red = True
    else:
        has_black = True
        
    for neighbour in adj[node]:
        if neighbour != parent:
            r, b = dfs(neighbour, node)
            if r : has_red = True
            if b : has_black = True
            
    if has_black and has_red:
        result[0] += 1
        
    return has_red, has_black

n = int(input())
colors = input().strip()
edges = [list(map(int, input().split())) for _ in range(n-1)]

adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
    
result = [0]
dfs(0, -1)
print(result[0])