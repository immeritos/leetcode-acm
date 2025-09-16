import sys
sys.setrecursionlimit(1_000_000)

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
depth = [0]*(n+1)
children = [[] for _ in range(n+1)]
max_depth = 0

def dfs(u, p):
    global max_depth
    for v in adj[u]:
        if v == p:
            continue
        depth[v] = depth[u] + 1
        max_depth = max(max_depth, depth[v])
        children[u].append(v)
        dfs(v, u)
        
dfs(1, 0)

answer = 0
for h in range(max_depth+1):
    by_depth = [[] for _ in range(max_depth+1)]
    for v in range(1, n+1):
        by_depth[depth[v]].append(v)
        
    best = [-10**9]*(n+1)
    for d in range(max_depth, -1, -1):
        for v in by_depth[d]:
            if depth[v] > h:
                best[v] = -10**9
            elif depth[v] == h:
                best[v] =1
            else:
                s = sum(best[u] for u in children[v] if best[u] > 0)
                best[v] = s + 1 if s > 0 else -10**9
    
    answer = max(answer, best[1])       
    
print(n - answer) 