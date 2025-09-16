"""
给定 n 个测试用例和 m 个代码模块，测试用例的覆盖情况用一个二维数组 casescases 表示，
其中 cases[i][j] 为 1 表示第 i 个测试用例覆盖了第 j 个模块，为 0 表示未覆盖。
要求找出一个最小的测试用例集合，使得该集合覆盖所有模块，即所有模块至少被一个测试用例覆盖。
如果不存在这样一个集合，则返回 -1。
"""
"""
输入：
3 2
1 0
1 0
1 0
"""
"""
输出：
-1
"""


import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    tests = []
    index = 0
    for i in range(n):
        mask = 0
        for j in range(m):
            x = int(input().split()[index])
            index += 1
            if x == 1:
                mask |= (1 << j)
        tests.append(mask)
        
    target = (1 << m) - 1
    ans = float('inf')
    
    for s in range(1 << n):
        union_mask = 0
        cnt = 0
        for i in range(n):
            if s & (1 << i):
                union_mask |= tests[i]
                cnt += 1
        if union_mask == target:
            ans = min(ans, cnt)
    
    print(-1 if ans == float('inf') else ans)

if __name__ == "__main__":
    main()           