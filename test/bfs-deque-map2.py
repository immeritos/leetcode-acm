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
import sys
input = sys.stdin.readline

def shortest_path(grid):
    m, n = len(grid), len(grid[0])
    dirs = [(-1, 0), (1,0), (0, -1), (0, 1)]

    # 1) 收集起点、终点、虫洞    
    holes = []
    sx = sy = tx = ty = -1
    for i in range(m):
        for j in range(n):
            c = grid[i][j]
            if c == '2':
                holes.append((i, j))
            elif c == 'S':
                sx, sy = i, j
            elif c == 'E':
                tx, ty = i, j

    # 2) 按出现顺序两两配对虫洞（(0,1), (2,3), ...）
    teleport = {}
    if len(holes) % 2 == 2:
        holes.pop()
    for i in range(0, len(holes), 2):
        a, b = holes[i], holes[i+1]
        teleport[a] = b
        teleport[b] = a
    
    INF = 10**18    
    dist = [[INF]*n for _ in range(m)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0
    
    while q:
        x, y = q.popleft()
        d = dist[x][y]

        # 到达终点
        if (x, y) == (tx, ty):
            return d
        
        # 3.1 四方向移动（代价 = 1）
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '1':
                if d + 1 < dist[nx][ny]:
                    dist[nx][ny] = d + 1
                    q.append((nx, ny))

        # 3.2 虫洞传送（代价 = 0）        
        if grid[x][y] == '2':
            tx2, ty2 = teleport[(x, y)]
            if d < dist[nx][ny]:
                dist[nx][ny] = d
                q.appendleft((tx2, ty2))  # 代价0 → 左端入队（更优先）
                
    return -1

if __name__ == "__main__":
    m, n = map(int, input().split())
    grid = [list(input().strip()) for _ in range(m)]
    print(shortest_path(grid))