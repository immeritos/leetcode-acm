"""
给定一个大小为 k*k 的二维矩阵 map[][], 表示二维空间中的一个地图, 其中 map[i][j] 表示位置 (i,j) 上的地形高度。
玩家控制一个角色从矩阵左上角位置 (0,0) 进入，从矩阵右侧任意位置出去。

角色在矩阵中只能向右或向下移动；
如果相邻两个节点高度差大于 1, 则角色不能移动过去；
角色通过 (i,j) 地点时, 会消耗 map[i][j] 的体力值。

要求计算最省体力值的路线所消耗的体力值.

若不存在可行路径, 返回 -1;
若参数不合法（包括 k<=0 或 k>100, 或任意 map[i][j] 不在 [0,10] 范围内）, 返回 -2。
"""
"""
输入：
3
1 2 3
5 5 5
7 7 7
"""
"""
输出：
6
"""

import sys
def main():
    k = int(input())
    if not k:
        return
    if k <= 0 or k >= 100:
        print(-2)
        return
    
    mp = []
    idx = 1
    for _ in range(k):
        row = list(map(int, input().split()))
        if any(v < 0 or v > 10 for v in row):
            print(-2)
            return
        mp.append(row)
        idx += k
        
    INF = 10**9
    dp = [[INF]*k for _ in range(k)]
    dp[0][0] = mp[0][0]
    
    for i in range(k):
        for j in range(k):
            if i>0 and abs(mp[i][j] - mp[i-1][j]) <= 1:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + mp[i][j])
            if j>0 and abd(mp[i][j] - mp[i][j-1]) <= 1:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + mp[i][j])
    
    ans = min(dp[i][k-1] for i in range(k))
    print(-1 if ans >= INF else ans)
    
if __name__ == "__main__":
    main()