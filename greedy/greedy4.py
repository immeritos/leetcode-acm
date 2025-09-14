def minCoins(coins, amount):
    coins.sort(reverse=True)
    
    coin_count = 0
    
    for coin in coins:
        if amount == 0:
            break
        coin_count += amount // coin
        amount %= coin
    
    if amount == 0:
        return coin_count
    else:
        return -1
    
n = int(input())
coins = list(map(int, input().split()))
amount = int(input())

print(minCoins(coins, amount))