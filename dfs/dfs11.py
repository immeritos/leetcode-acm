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