"""
给定一个由 m*n 个单元格组成的矩阵, 每个单元格有一个高度值(范围为1到2^31-1)。
你可以从任意单元格开始, 向上下左右四个方向滑动, 每次只能滑向高度严格更低的相邻单元格, 且不能重复访问已走过的格子。
求满足规则的最长滑行路径长度。
"""
"""
输入：
3 3
9 8 7
6 6 6
6 6 6
"""
"""
输出：
4
"""

from functools import lru_cache
import sys
sys.setrecursionlimit(1_000_000)

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

@lru_cache(None)
def dfs(i, j):
    best = 1
    for dx, dy in dirs:
        nx, ny = i + dx, j + dy
        if 0 <= x < m and 0 <= y < n and matrix[nx][ny] < matrix[i][j]:
            best = max(best, 1+dfs(x, y))
    return best

ans = max(dfs(i, j) for i in range(m) for j in range(n))
print(ans)