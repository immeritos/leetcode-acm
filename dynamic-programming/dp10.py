s = input()
n = len(s)
dp = [[0] * 10 for _ in range(n+1)]
mod = 10 ** 9 + 7
dp[0][int(s[0])] = 1
for i in range(1, n):
    tot = 0
    now = int(s[i])
    for j in range(10):
        if j != now:
            dp[i][j] = dp[i-1][j]
        
        tot = (tot + dp[i-1][j]) % mod
        
    dp[i][now] = (tot - dp[i - 1][now] + 1 + mod) % mod
    
print(sum(dp[n-1]) % mod)