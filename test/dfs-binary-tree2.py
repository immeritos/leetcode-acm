"""
给定一棵以节点 1 为根的树型网络, 包含 n 台设备（节点编号 1 到 n)。
网络中任意两节点通过边相连, 最后没有子节点的称为“边缘设备”。
希望移除尽可能少的节点, 使得剩下网络中所有边缘设备到根设备的距离都相同。
输出最少需要移除的节点数。
"""
"""
输入：
7
1 2
1 3
2 4
2 5
4 6
4 7
"""
"""
输出：
2
"""

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