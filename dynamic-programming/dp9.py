t = int(input())
results = []

for _ in range(t):
    n, k = map(int, input().split())
    
    a = list(map(int, input().split()))
    
    MIN_VALUE = float('-inf')
    dp = MIN_VALUE * (n + 2)
    pre = MIN_VALUE * (n + 2)
    udp = MIN_VALUE * (n + 2)
    suf = MIN_VALUE * (n + 2)
    
    for i in range(1, n + 1):
        dp[i] = max(a[i-1], dp[i-1]+a[i-1])
        
    for i in range(1, n + 1):
        pre[i] = max(dp[i], pre[i-1])
    
    for i in range(n, 0, -1):
        udp[i] = max(dp[i], udp[i+1] + a[i - 1])
        
    res = MIN_VALUE
    for i in range(1, n - k + 1):
        res = max(res, pre[i] + suf[i + k + 1])
        
    results.append(res)
    
print('\n'.join(map(str, results)))