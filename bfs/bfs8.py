import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

g = {}
roots = []
for _ in range(n):
    x, y = input().split()
    if y == "NA":
        roots.append(x)
    else:
        g.setdefault(y, []).append(x)
        
q = deque()
for r in roots:
    q.append((r, 1))
    
best = 0
ans = set()
while q:
    u, d = q.popleft()
    if d > best:
        best = d
        ans = {u}
    elif d = best:
        ans.add(u)
    for v in g.get(u, ()):
        q.append((v, d+1))

print(" ".join(sorted(ans)))