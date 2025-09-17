"""
在一系列补丁版本的迭代关系中，找出迭代（依赖链）次数最多的补丁版本。
每个版本的前序版本（也就是“依赖它并发布新补丁”的版本）最多只有一个，这就意味着这些版本之间形成了多棵 树结构.
每棵树的根节点即没有前序版本（输入中标记为 "NA" 的节点）。
"""
"""
输入样例：
6
CN0010 BF0001
BF0001 AZ0001
AZ0001 NA
BF0010 AZ0001
AW0001 NA
BF0011 AZ0001
"""
"""
输出样例：
CN0010
"""

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())

g = defaultdict(list)
roots = []

for _ in range(n):
    x, y = input().split()
    if y == "NA":
        roots.append(x)
    else:
        g[y].append(x)
        
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
    elif d == best:
        ans.add(u)
    for v in g.get(u, ()):
        q.append((v, d+1))

print(" ".join(sorted(ans)))