"""
给定长度为 N 的数组 crossroads[], 其中 crossroads[i] 表示第 i 号路口基站的当前接入人数；以及覆盖范围 k。
基站 i 可覆盖路口 [max(0, i-k) … min(N-1, i+k)]。
小明从 0 号路口出发, 走过第 i 段路（路口 i 到 i+1 之间）时, 可连接所有覆盖该路段的基站, 需选择接入人数最少的基站。
返回长度为 N-1 的数组 ret, 其中 ret[i] 为第 i 段路的最佳基站编号。
"""
"""
输入：
3 5 8 7 6 7 4
2
"""
"""
输出：
0 0 1 4 6 6 
"""

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