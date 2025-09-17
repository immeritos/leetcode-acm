"""
给定一个地铁线路网络, 其中有N个站点(3<=N<=20)以及各个相邻站点之间的乘坐时间。输入中：

- 第一行为站点总数N;
- 第二行为乘客的出发站s和到达站t;
- 接下来的若干行每行给出两个站点和它们之间的乘坐时间, 输入持续到出现结束符"0000"为止。

本题中地铁网络被视为无向图, 即每条输入的边可以双向使用。保证输入中起点与终点之间存在唯一一条耗时最短的路径。
要求程序输出由各站点名称组成、以空格分隔的完整最短路径线路。
"""
"""
输入样例：
12
a e
a b 2
b c 2
c d 2
d e 2
f b 3
b g 3
g h 2
h i 3
j h 2 
h e 3
e k 2
k l 4
0000
"""
"""
输出样例：
a b c d e
"""

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def main():
    INF = 10**18
    
    n = int(input().strip())
    start, end = input().split()

    g = defaultdict(list)
    while True:
        line = input().strip()
        if not line:
            break
        if line == "0000":
            break
        u, v, w = line.split()
        w = int(w)
        g[u].append((v, w))
        g[v].append((u, w))
        
    dist = defaultdict(lambda: INF)
    prev = {}
    dist[start] = 0

    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        if u == end:
            break
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
            
    if dist[end] == INF:
        print("NO PATH")
        return

    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = prev[cur]
    path.append(start)
    path.reverse()

    print(" ".join(path))
    
if __name__ == "__main__":
    main()