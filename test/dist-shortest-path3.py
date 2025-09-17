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

INF = float('inf')
def shortest_path(src, N, g):
    dist = [INF] * N
    dist[src] = 0
    pq = [(0, src)]  # (距离, 节点)

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v in range(N):
            w = g[u][v]
            if w == 0:
                continue  # 不相邻
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def main():
    # 读入
    N = int(input().strip())
    g = [list(map(int, input().split())) for _ in range(N)]
    is_ent = list(map(int, input().split()))
    S, T = map(int, input().split())
    
    if is_ent[S] != 1 or is_ent[T] != 1:
        print("NO PATH")
        return 
    
    distS = shortest_path(S, N, g)
    distT = shortest_path(T, N, g)
    L = distS[T]
    if L >= INF:
        print("NO PATH")
        return
    
    path = [S]
    u = S
    while u != T:
        nxt = None
        for v in range(N):
            w = g[u][v]
            if w == 0:
                continue
            if distS[u] + w + distT[v] == L:
                nxt = v  # 第一个满足的就是编号最小
                break
        
        if nxt is None:
            print("NO PATH")
            return
        path.append(nxt)
        u = nxt
    print(*path)

if __name__ == "__main__":
    main()