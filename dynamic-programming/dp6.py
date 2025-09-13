n = int(input())
coins = list(map(int, input().split()))
amount = int(input())

dp = [float('inf')] * (amount + 1)
dp[0] = 0

for coin in coins:
    for x in range(coin, amount + 1):
        if dp[x - coin] + 1 < dp[x]:
            dp[x] = dp[x - coin] + 1
            
if dp[amount] == float('inf'):
    print(-1)
else:
    print(dp[amount])