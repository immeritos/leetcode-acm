"""
我们可以将山脉地图看成一个二维网格, 每个格子代表一个节点, 相邻(上、下、左、右) 格子之间有边相连。由于每步移动代价相同(均为 1) , 并且我们要找从山底到山峰的最少步数, 最合适的算法是 广度优先搜索(BFS) 。

具体步骤如下: 

    1. 扫描地图, 找到山底起点 start(高度为 0 的唯一坐标) 和山峰终点 target(最高高度的唯一坐标) 。
    2. 初始化队列, 将 start 入队, 并用一个与地图同型的布尔数组 vis 记录访问状态。
    3. BFS 过程: 
        - 每次从队列取出当前格子 (x,y) 及其已走步数 d。
        - 枚举四个方向的新坐标 (nx,ny), 判断是否越界、未访问, 并且满足高度差限制: 
            - 向高处移动: grid[nx][ny] - grid[x][y] ≤ climbAbility
            - 向低处移动: grid[x][y] - grid[nx][ny] ≤ climbAbility
        - 若满足, 则将 (nx,ny) 标记为已访问并入队, 步数 d+1。
        - 若 (nx,ny) 为 target, 即可立即返回 d+1。
    4.若 BFS 结束仍未到达山峰, 返回 -1。
"""
"""
输入：
2
3 2
1 3
0 4
5 3
"""
"""
输出：
5
"""

from collections import deque

def min_steps(grid, ability):
    n, m = len(grid), len(grid[0])
    
    start = target = None
    max_h = -1
    for i in range(n):
        for j in range(m):
            h = grid[i][j]
            if h == 0:
                start = (i, j)
            if h > max_h:
                max_h, target = h, (i, j)
    
    vis = [[False]*m for _ in range(n)]
    q = deque()
    q.append((*start, 0))
    vis[start[0][start[1]]] = True
    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y, d = q.popleft()
        if (x, y) == target:
            return d
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny]:
                diff = grid[nx][ny] - grid[x][y]
                if abs(diff) <= ability:
                    vis[nx][ny] = True
                    q.append((nx, ny, d+1))
    return -1

if __name__ == "__main__":
    ability = int(input().strip())
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(min_steps(grid, ability))