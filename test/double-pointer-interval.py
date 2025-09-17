"""
给定一个整数数组array, 代表一系列时间点上的信号强度值。请在这些时间点中找出一个波峰区间 [i,j](其中i<=j), 满足以下两个连续阶段：

    区间前半段是单调非递减
    区间后半段是单调非递增

必须同时出现两个阶段才能构成一个合法的波峰区间！

找出所有合法波峰区间中, 最大值与最小值的差值最大的那个区间, 返回这个最大差值。
"""
"""
输入：
6
3 8 12 10 6 9
"""
"""
输出：
9
"""
def max_peak_diff(array):
    n = len(array)
    if n==0:
        return 0
    
    left = [0]*n
    for i in range(n):
        if i>0 and array[i-1] <= array[i]:
            left[i] = left[i-1]
        else:
            left[i] = i
    
    right = [0]*n
    right[-1] = n-1
    for i in range(n-2, -1, -1):
        if array[i] >= array[i+1]:
            right[i] = right[i+1]
        else:
            right[i] = i
    
    ans = 0
    for i in range(n):
        L, R = left[i], right[i]
        if L < i and R > i:
            ans = max(ans, array[i] - min(array[L], array[R]))
            
    return ans
            

if __name__ == "__main__":
    m = int(input())
    array = list(map(int, input().split()))
    print(max_peak_diff(array))
