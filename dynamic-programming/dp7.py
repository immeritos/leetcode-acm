MOD = 10**9 + 7

n = int(input())

dp = [[0]*(n+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(n + 1):
    for j in range(n + 1):
        dp[i][j] = dp[i-1][j]
        if j >= i:
            dp[i][j] = (dp[i][j] + dp[i][j-i]) % MOD
            
print(dp[n][n])