"""Given a maze represented by a two-dimensional matrix, it contains walls and paths. 
1 in the matrix represents a wall, and 0 represents a path. The starting and ending points are also given. 
The question is whether there is a path from the starting point to the ending point that allows movement through the maze. 
You can move in four directions: up, down, left, and right, but you cannot pass through walls.
"""
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, x1, y1, x2, y2, n, m):
    
    if grid[x1][y1] == 1 or grid[x2][y2] == 1:
        return -1
    
    visited = [[False] * m for _ in range(n)]
    
    q = deque()
    q.append((x1, y1))
    visited[x1][y1] = True
    
    while q:
        x, y = q.popleft()
        
        if (x, y) == (x2, y2):
            return True
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < n and 0 <= ny < n and \
                grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    
    return -1

def main():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    x1, y1, x2, y2 = map(int, input().split())
    
    ans = bfs(grid, x1, y1, x2, y2, n, m)
    
    if ans == -1:
        print("NO")
    else:
        print("YES")
        
if __name__ == "__main__":
    main()