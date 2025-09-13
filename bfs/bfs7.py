"""
Find the minimum number of times 1 can be converted to b (output -1 if no change is possible).
There are two operations:
1. Multiply the current number by a
2. Circularly shift the current number right once (12345 -> 51234) (12345 -> 51234)
"""

import sys
from collections import deque
input = sys.stdin.readline

def rotate_right(x):
    if x < 10 or x % 10 == 0:
        return -1
    s = str(x)
    return int(s[-1] + s[:-1])

def min_steps(a, b):
    if b == 1:
        return 0
    
    MAXV = 10 ** len(str(b)) - 1
    
    q = deque([1])
    visited = {1: 0}
    
    while q:
        cur = q.popleft()
        step = visited[cur]
        
        nxt = cur * a
        if nxt <= MAXV and nxt not in visited:
            visited[nxt] = step + 1
            if nxt == b:
                return step + 1
            q.append(nxt)
            
            
            rot = rotate_right(cur)
            if rot != -1 and rot <= MAXV and rot not in visited:
                visited[rot] = step + 1
                if rot == b:
                    return step + 1
                q.append(rot)
    
    return -1

def main():
    a, b = map(int, input().split())
    print(min_steps(a, b))
    
if __name__ == "__main__":
    main()