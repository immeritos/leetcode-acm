"""
物流公司总部位于编号为 1 的地点，城市共有 N 个地点、N-1 条连通所有地点的公路。
今天有 M 条寄送任务，每条任务都由一个寄件地 s 和一个收件地 t(均在 2<=s,t<=N, 且 s≠t)组成。

运输车工作流程分两阶段：

    收件阶段: 从总部(1)出发，按任意顺序跑到所有寄件地点 {si}，收取货物后回到总部(1)扫描。
    送件阶段: 从总部(1)出发，按任意顺序将扫描后的货物送到所有送件地点 {ti}，送完后回总部(1)。

要求: 求完成所有任务时运输车最少行驶的总里程。任务的先后顺序可任意安排。
"""
"""
输入：
4 2 
2 1 1
1 3 2
4 3 2
3 2 
4 2
"""
"""
输出：
10
"""

from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    # 1) BFS rooting：父亲与父边权        
    fa = [0] * (N+1)
    pw = [0] * (N+1)
    order = []
    q = deque([1])
    visited = [False] * (N+1)
    visited[1] = True
    
    while q:
        u = q.popleft()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                fa[v] = u
                pw[v] = w
                q.append(v)
                
    # 2) 统计子树是否包含 S/T（布尔即可）    
    hasS = [False] * (N+1)
    hasT = [False] * (N+1)
    for _ in range(M):
        s, t = map(int, input().split())
        hasS[s] = True
        hasT[t] = True
        
    for u in reversed(order[1:]): # 把层序结果反过来
        p = fa[u]
        hasS[p] |= hasS[u]
        hasT[p] |= hasT[u]
        
    sumS = sum(pw[u] for u in range(2, N+1) if hasS[u])
    sumT = sum(pw[u] for u in range(2, N+1) if hasT[u])
    ans = 2 * (sumS + sumT)
    print(ans)
    
if __name__ == "__main__":
    main()