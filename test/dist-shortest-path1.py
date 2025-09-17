"""
给定一个救援物资集结点（编号为 0)和 N 个受灾乡镇（编号为 1 到 N)，以及它们之间的距离矩阵。矩阵大小为 (N+1)*(N+1)，其中元素 d_{ij}表示节点 i 到节点 j 的距离，不相邻时为 0。
现在要求从节点 0 到指定乡镇节点 m 的最短路径长度。
"""
"""
输入：
5
0 5 13 0 0 0
5 0 12 0 75 0
13 12 0 25 0 0
0 0 25 0 35 20
0 75 0 35 0 40
0 0 0 20 40 0
3
"""
"""
输出：
38
"""

import sys
def main():
    N = int(input().strip())
    total = N + 1
    d = [list(map(int, input().split())) for _ in range(total)]
    m = int(input().strip())
    
    INF = 10**9
    dist = [INF]*total
    vis = [False]*total
    
    dist[0] = 0
    
    for _ in range(total):
        u = -1
        minDist = INF
        for i in range(total):
            if not vis[i] and dist[i] < minDist:
                u = i
                minDist = dist[i]
        if u == -1:
            break
        vis[u] = True
        for v in range(total):
            if not vis[v] and d[u][v] > 0 and dist[v] > dist[u] + d[u][v]:
                dist[v] = dist[u] + d[u][v]
                
    print(dist[m])
    
if __name__ == "__main__":
    main()