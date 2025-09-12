"""
Problem Description:

Given a two-dimensional grid of size n * n. 
You start at coordinate (sx,sy) and are allowed to move in one of four directions at a time: up, down, left, or right. 
Each move takes 1 steps. Now given a target coordinate (ex,ey).
Determine the number of different paths you can take to reach the target location (ex,ey) in at most k steps.

Note that you can choose to stop at any time; you don't have to reach the target in exactly k steps.
"""
"""
Input:

The first line contains an integer nn, representing the size of the grid (1 <= n <= 10).

The second line inputs four integers sx,sy,ex,ey, 
representing the coordinates of the starting point (sx,sy) and the end point (ex,ey) (1 <= sx, ex <= n, 1 <= sy, ey <= n).

The third line inputs an integer k, representing the maximum number of steps (1 <= k <= 10).
"""
"""
Output:

Output an integer representing the number of different paths from (sx,sy) to (ex,ey) in at most k steps.
"""

countPaths = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, steps, n, sx, sy, ex, ey, k):
    global countPaths
    
    if x == ex and y == ey:
        countPaths += 1
        
    if steps == k:
        return
    
    for dir in range(4):
        newX = x + dx[dir]
        newY = y + dy[dir]
        
        if 1 <= newX <= n and 1 <= newY <= n:
            dfs(newX, newY, steps + 1, n, sx, sy, ex, ey, k)
            
if __name__ == "__main__":
    n = int(input())
    sx, sy, ex, ey = map(int, input().split())
    k = int(input())
    
    dfs(sx, sy, 0, n, sx, sy, ex, ey, k)
    
    print(countPaths)