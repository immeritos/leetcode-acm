"""
In Tetris, there are only 1 large blocks, each made up of four smaller square blocks. 
Now, calculate the maximum number of large blocks that can be placed within a given grid size. 
The specific rules are as follows:
1. The grid is a square grid.

2. Blocks cannot overlap.

3. Blocks cannot extend beyond the grid boundaries.

4. Blocks cannot be placed in certain positions within the grid.
"""

import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline()

def main():
    n, k = map(int, input().split())
    
    vis = [[False] * n for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        vis[x][y] = True
    
    total_pos = (n - 1) * (n - 1)
    
    def dfs(idx):
        if idx == total_pos:
            return 0
        
        r = idx // (n - 1)
        c = idx % (n - 1)
        
        best = dfs(idx + 1)
        
        if (not vis[r][c] and not vis[r+1][c] and
            not vis[r][c+1] and not vis[r+1][c+1]):
            vis[r][c] = vis[r+1][c] = vis[r][c+1] = vis[r+1][c+1] = True
            
            best = max(best, 1 + dfs(idx + 1))
            
            vis[r][c] = vis[r+1][c] = vis[r][c+1] = vis[r+1][c+1] = False
        
        return best
    
    print(dfs(0))
    
if __name__ == "__main__":
    main()