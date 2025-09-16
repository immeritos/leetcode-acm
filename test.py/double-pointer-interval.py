"""
给定一个整数数组arrayarray, 代表一系列时间点上的信号强度值。请在这些时间点中找出一个波峰区间 [i,j](其中i<=j), 满足以下两个连续阶段：

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
    ans = 0

    for mid in range(n):
        L = mid
        while L > 0 and array[L - 1] <= array[L]:
            L -= 1

        R = mid
        while R + 1 < n and array[R] >= array[R + 1]:
            R += 1

        # 必须两边都扩展了，才是合法波峰
        if L < mid and R > mid:
            peak = array[mid]
            low = min(array[L], array[R])
            ans = max(ans, peak - low)

    return ans

if __name__ == "__main__":
    m = int(input())
    array = list(map(int, input().split()))
    print(max_peak_diff(array))
