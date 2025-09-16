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