"""
给定一个长度为n的整数数组a(元素可为正、负或零），你拥有一次“取反”操作的能力：
可以任选一个连续子数组，将其中每个元素都变为相反数。该操作最多执行一次(也可不执行）。
操作之后，你再任选一个非空的连续子数组，取其元素之和。
问：通过恰当地选择取反区间(或不取反）以及最后取和的区间，能够获得的最大子数组和是多少？
"""
"""
输入：
6
3 1 -6 2 -5 3
"""
"""
输出：
16
"""

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