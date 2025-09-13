"""
Given an m * n 2D matrix, where each element represents a square. Each square in the matrix can be either blank (represented by 0) or a wall (represented by 1). 
You need to find the shortest path length from a given starting point to a destination.

You can move from the current square in any of four directions: up, down, left, or right. 
You can only move to adjacent blank squares. If the destination cannot be reached, return -1.
"""

from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, x1, y1, x2, y2, m, n):
    if grid[x1][y1] == 1 or grid[x2][y2] == 1:
        return -1
    
    visited = [[False] * n for _ in range(m)]
    q = deque([(x1, y1, 0)])
    visited[x1][y1] = True
    
    while q:
        x, y, dist = q.popleft()
        
        if (x, y) == (x2, y2):
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n and \
                grid[nx][ny] == 0 and not visited[nx][ny]:
                    q.append([nx, ny, dist + 1])
                    visited[nx][ny] = True
                    
    return -1

def main():
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
        
    x1, y1 = map(int, input().split())
    x2,  y2 = map(int, input().split())
    
    result = bfs(grid, x1, y1, x2, y2, m, n)
    
    print(result)

if __name__ == "__main__":
    main()    