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
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
depth = [0]*(n+1)
children = [[] for _ in range(n+1)]
max_depth = 0

def dfs_root(u, p):
    """把树在 1 处定根，同时统计 depth / children / max_depth。"""
    global max_depth
    for v in adj[u]:
        if v == p:
            continue
        depth[v] = depth[u] + 1
        max_depth = max(max_depth, depth[v])
        children[u].append(v)
        dfs_root(v, u)
        
dfs_root(1, 0)

# 预先把各层的节点分组
by_depth = [[] for _ in range(max_depth+1)]
for v in range(1, n+1):
    by_depth[depth[v]].append(v)
    
NEG_INF = -10**15
answer = 0
for h in range(max_depth+1):    
    # best[v]: 在以 v 为根的“保留子树”中，若所有叶子深度都等于 h，则最多能保留多少节点；
    # 否则为 NEG_INF 表示不可行。    
    best = [NEG_INF]*(n+1)
    
    # 从底层往上合并
    for d in range(max_depth, -1, -1):
        for v in by_depth[d]:
            if depth[v] > h:
                best[v] = NEG_INF
            elif depth[v] == h:
                best[v] = 1
            else:
                # 必须从孩子里选择“非空的、可行的”子树，并把它们并起来（并列子树的叶深相同为 h）
                subtotal = 0
                for u in children[v]:
                    if best[u] > 0:
                        subtotal += best[u]
                best[v] = subtotal + 1 if subtotal > 0 else NEG_INF
    
    if best[1] > answer:
        answer = best[1]    
    
print(n - answer) 