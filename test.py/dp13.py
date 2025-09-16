def max_subarray_with_one_flip(a):
    dp0 = a[0]
    dp1 = -a[0]
    dp2 = a[0]
    ans = max(dp0, dp1, dp2)
    
    for x in a[1:]:
        prev0, prev1, prev2 = dp0, dp1, dp2
        
        dp0 = max(prev0 + x, x)
        dp1 = max(prev1 - x, prev0 - x)
        dp2 = max(prev2 + x, prev1 + x)
        
        ans = max(ans, dp0, dp1, dp2)
        
    return ans

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_subarray_with_one_flip(arr))