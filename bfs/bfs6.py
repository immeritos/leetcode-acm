"""
In an N * N maze, a delivery person starts at the top left corner and aims to reach the bottom right corner.
They can move in four directions: up, down, left, and right. 
Each move to an adjacent square takes 1 unit of time, and they must reach their destination in at most K units of time.
Each square has a radiation value, and the delivery person needs to wear protective clothing with a radiation protection level no lower than that value to pass through it.
Thus, the delivery person wants to know the minimum protective level required to ensure they can reach their destination safely and meet the time limit.
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(limit, a, n, k):
    if a[0][0] > limit or a[n-1][n-1] > limit:
        return False
    
    q = deque([(0, 0, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y, step = q.popleft()
        if step > k:
            continue
        if x == n-1 and y == n-1:
            return True
        ns = step + 1
        if ns > k:
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and \
                a[nx][ny] <= limit and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, ns))
    
    return False

def main():
    n = int(input().strip())
    k = int(input().strip())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    left = max(a[0][0], a[n-1][n-1])
    right = max(max(row) for row in a)
    
    if not bfs(right, a, n, k):
        print(-1)
        sys.exit(0)
    
    ans  = right
    while (left <= right):
        mid = (left + right) // 2
        if bfs(mid, a, n, k):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    print(ans)
    
if __name__ == "__main__":
    main()
    