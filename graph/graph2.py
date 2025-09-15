import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
start, end = input().split()

g = defaultdict(list)
while True:
    line = input().strip()
    if line == "0000":
        break
    u, v, w = line.split()
    w = int(w)
    g[u].append((v, w))
    g[v].append((u, w))
    
INF = float('inf')
dist = defaultdict(lambda: INF)
prev = {}
dist[start] = 0

pq = [(0, start)]
while pq:
    d, u = headq.heappop(pq)
    if d != dist[u]:
        continue
    for v, w in g[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            prev[v] = u
            heapq.heappush(pq, (nd, v))
        
if dist[end] == INF:
    print("NO PATH")
else:
    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = prev[cur]
    path.append(start)
    path.reverse()

print(" ".join(path))