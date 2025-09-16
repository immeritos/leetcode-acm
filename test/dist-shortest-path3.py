"""
给定一个公园中的 N 个景点（编号从 0 到 N-1), 以及一个 N*N 的距离矩阵， 矩阵中第 i 行第 j 列的元素表示景点 i 到景点 j 的距离， 距离为 0 表示不相邻。
还有一行标记哪些景点是公园的出入口（用 1 表示是， 0 表示否）。
最后给定一个入口景点编号 S 和一个出口景点编号 T。
要求在允许经过任意其他景点但不需要访问所有景点的前提下， 找到从 S 到 T 的最短游园线路， 并输出具体经过的景点序列。
如果存在多条等长最短路径， 则输出按景点序号从小到大最小的那条路径。
"""
"""
输入：
3
0 2 4
2 0 3
4 3 0
1 0 1
0 2
"""
"""
输出：
0 2
"""

import heapq

def shortest_path(N, g, is_entrance, S, T):
    INF = float('inf')
    dist = [INF] * N
    paths = [[] for _ in range(N)]

    dist[S] = 0
    paths[S] = [S]
    pq = [(0, S)]  # (距离, 节点)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v in range(N):
            if g[u][v] == 0:
                continue  # 不相邻
            nd = d + g[u][v]
            new_path = paths[u] + [v]
            # 如果新的距离更短， 或距离相同但字典序更小，则更新
            if nd < dist[v] or (nd == dist[v] and new_path < paths[v]):
                dist[v] = nd
                paths[v] = new_path
                heapq.heappush(pq, (nd, v))
    return paths[T]

# 读入
N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]
is_entrance = list(map(int, input().split()))
S, T = map(int, input().split())

# 计算并输出
res = shortest_path(N, g, is_entrance, S, T)
print(' '.join(map(str, res)))
