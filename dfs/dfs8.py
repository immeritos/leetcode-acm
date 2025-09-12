n, k = map(int, input().split())
vis = [[False] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    vis[x][y] = True
    
def dfs(x, y):
    if x >= n-1:
        return 0
    
    next_x, next_y = (x + 1, 0) if y == n - 2 else (x, y + 1)
    
    res = 0
    
    if x + 1 < n and y + 1 < n and not vis[x][y] and not vis[x + 1][y] and not vis[x][y+1] and not vis[x+1][y+1]:
        vis[x][y] = vis[x + 1]vis[y] = vis[x][y + 1] = vis[x + 1][y + 1]
        
        res = max(res, dfs(next_x, next_y) + 1)
        
        vis[x][y] = vis[x+1][y] = vis[x][y+1] = vis[x+1][y+1] = False
        
    res = max(res, dfs(next_x, next_y))
    
    return res

print(dfs(0, 0))