"""
给定一个大小为m*n的网格, 每个格子上可能放置一个无线接入点（用值 1 表示）或不放置（用值 0 表示）。
如果两个无线接入点的覆盖区域相连, 则它们属于同一个子网。
邻接关系包括上下左右以及四个对角方向（共 8 个方向）。现要求通过光纤将不同的子网两两相连, 即如果共有k个子网, 则需要建立k(k-1)/2 条链路。
请计算给定网格中所有子网两两相连需要多少条光纤链路。
"""
"""
输入：
4 5
1 1 0 0 0
0 0 0 0 0
0 0 1 1 0
0 0 0 1 0
"""
"""
输出：
1
"""

import sys
from collections import deque
input = sys.stdin.readline

def main():
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    
    visited = [[False] * n for _ in range(m)]
    dirs = [(-1, -1), (-1, 0), (-1, 1), 
            (0, -1),            (0, 1), 
            (1, -1), (1, 0), (1, 1)]
    count = 0
    dq = deque()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                count += 1
                visited[i][j] = True
                dq.append((i, j))
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            if grid[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                dq.append((nx, ny))
                                
    k = count
    ans = k * (k-1) // 2
    print(ans)
    
if __name__ == "__main__":
    main()    