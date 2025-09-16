from collections import deque
import sys

def best_station(cross, k):
    n = len(cross)
    if n<2 or k<1 or k>n:
        return -1
    dq = deque()
    res = []
    R = -1
    for i in range(n-1):
        L = max(0, i+1-k)
        newR = min(n-1, i+k)
        while R < newR:
            R += 1
            while dq and cross[dq[-1]] >= cross[R]:
                dq.pop()
            dq.append(R)
        while dq and dq[0] < L:
            dq.popleft()
        res.append(dp[0])
        
    return res

if __name__ == "__main__":
    cross = list(map(int, input().split()))
    k = int(input().strip())
    if not cross or not k:
        print(-1)
        sys.exit(-1)
    ans = best_station(cross, k)
    if ans == -1:
        print(-1)
    else:
        print(" ".join(map(str, ans)))