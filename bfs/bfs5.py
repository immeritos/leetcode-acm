"""
In a matrix of m rows and n columns, sanitation workers are required to deliver household waste from residential communities to the nearest recycling station. 
The matrix elements are:

0: Waste disposal station
1: Residential community
2: Empty area
-1: Obstructed area

The distance between adjacent points is 1, and movement is limited to up, down, left, and right. 
Calculate the minimum sum of the distances required to deliver waste from all residential communities to the recycling station. 
If there are no residential communities or recycling stations in the matrix, return 0. 
Residential communities that cannot reach the recycling station are not included in the distance sum.
"""

import sys
from collections import deque

def min_total_distance(grid, n, m):
    has_home = any(1 in row for row in grid)
    has_station = any(0 in row for row in grid)
    
    if not has_home or not has_station:
        return 0
    
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j))
                
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] != -1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))    
    
    total = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and dist[i][j] != -1:
                total += dist[i][j]
                
    return total

def main():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    ans = min_total_distance(grid, n, m)
    print(ans)
    
if __name__ == "__main__":
    main()