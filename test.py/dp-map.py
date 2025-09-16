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