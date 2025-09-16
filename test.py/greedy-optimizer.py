"""
给定长度为NN的数组 pvs, 其中pvs[i]=1表示位置i有光伏板, pvs[i]=0表示位置i为空。
现在可以在空位上安装“光伏优化器”, 只要一个光伏板的左边或者右边有优化器, 该光伏板就能提升发电效率。
请计算最少需要安装多少个优化器, 才能使所有光伏板都能被提升；如果无法覆盖所有光伏板, 则返回-1。
"""
"""
输入：
5
0 1 0 1 0
"""
"""
输出：
1
"""

def min_optimizers(pvs):
    n = len(pvs)
    covered = [False] * n
    has_opt = [False] * n
    ans = 0
    
    for i in range(n):
        if pvs[i] == i and not covered[i]:
            if i+1<n and p[i+1] == 0 and not has_opt[i+1]:
                has_opt[i+1] = True
                ans += 1
                covered[i] = True
                if i+2 < n and pvs[i+2] == 1:
                    covered[i+2] = True
            elif i-1>=0 and pvs[i-1] == 0 and not has_opt[i-1]:
                has_opt[i-1] = True
                ans += 1
                covered[i] = True
                if i-2 >= 0 and pvs[i-2] == 1:
                    covered[i-2] = True
            else:
                return -1
    return ans

if __name__ == "__main__":
    N = int(input().strip())
    pvs = list(map(int, input().split()))
    print(min_optimizers(pvs))