"""
给定一个迷官的地图，地图是一个二维矩阵，其中 0 表示通道, 1 表示墙壁, s 表示起点, E 表示终点。
你需要从起点 S 出发, 通过最路径到达终点 E , 返回最短路径的步数, 如果无法到达终点, 则返回 -1, 迷宫中会有虫洞, 用数字 2 表示, 成对出现, 你走入虫洞可以穿越到另一个虫洞出口, 耗费 0 步。

你只能上下左右移动, 并且不能走出迷官的边界, 也不能穿越墙壁.
"""
"""
输入：
5 5
S0000
11110
01010
01010
0000E
"""
"""
输出：
3 3
S00
111
E00
"""

from collections import deque

def shortest_path(grid):
    m, n = len(grid), len(grid[0])
    dirs = [(-1, 0), (1,0), (0, -1), (0, 1)]
    holes = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "2":
                holes.append((i, j))
            elif gird[i][j] == "S":
                sx, sy = i, j
    teleport = {}
    for i in range(0, len(holes), 2):
        a, b = holes[i], holes[i+1]
        teleport[a] = b
        teleport[b] = a
        
    vis = [[False]*n for _ in range(m)]
    q = deque()
    q.append((sx, sy, 0))
    vis[sx][sy] = True
    
    while q:
        x, y, d = q.popleft()
        if grid[x][y] == 'E':
            return d
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and \
                grid[nx][ny] != '1' and not vis[nx][ny]:
                    vis[nx][ny] = True
                    q.append((nx, ny, d+1))
        
        if grid[x][y] == '2':
            tx, ty = teleport[(x, y)]
            if not vis[tx][ty]:
                vis[tx][ty] = True
                q.append((tx, ty, d))
                
    return -1

if __name__ == "__main__":
    m, n = map(int, input().split())
    gird = [list(input().strip()) for _ in range(m)]
    print(shortest_path(grid))