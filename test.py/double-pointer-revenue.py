def max_revenue(n, K, revenues, manpowers):
    ans = 0
    cur_rev = 0
    cur_man = 0
    left = 0
    
    for right in range(n):
        cur_rev += revenues[right]
        cur_man = manpowers[right]
        while cur_man > K:
            cur_rev -= revenues[left]
            cur_man -= manpowers[left]
            left += 1
        ans = max(ans, cur_rev)
    return ans

if __name__ == "__main__":
    n, K = map(int, input().split())
    revenues = []
    manpowers = []
    for _ in range(n):
        r, m = map(int, input().split())
        revenues.append(r)
        manpowers.append(m)
    print(max_revenue(n, K, revenues, manpowers))