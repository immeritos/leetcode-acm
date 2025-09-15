import sys
from collections import deque
input = sys.stdin.readline

def main():
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    
    visited = [[False] * n for _ in range(m)]
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    dq = deque()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                count += 1
                visited[i][j] = True
                dq.append((i, j))
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <= and 0 <= ny < n:
                            if grid[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny]
                                dq.append((nx, ny))
                                
    k = count
    ans = k * (k-1) // 2
    print(ans)
    
if __name__ == "__main__":
    main()    