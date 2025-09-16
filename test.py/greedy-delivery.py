"""
某公司有 2 个仓库(用 A 和 B 表示)，需要给 m ( m 为偶数)个营业网点各配送一件货物。
假设每个仓库正好都有 m/2 件货物，配送给不同营业网点的费用使用一个二维数组 cost 表示，其中 cost[i]=[A_i,B_i)表示第 i 个营业网点从 A 仓发货的运费为 A_i ，从 B 仓库发货的费用为 B_i 。
请计算 m 件货物配送的最低费用，要求每个营业网点都有一件货物送到。
"""
"""
输入：
2
[[10,30],[30,200]]
"""
"""
输出：
60
"""

import sys

def main():
    m = int(input().strip())
    line = input().strip()
    
    nums = []
    num = 0
    in_num = False
    for c in line:
        if c.isdigit():
            num = num * 10 + int(c)
            in_num = True
        elif in_num:
            nums.append(num)
            num = 0
            in_num = False
    if in_num:
        nums.append(num)
        
    cost = [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]
    
    sumA = sum(a for a, b, in cost)
    diffs = sorted(b - a for a, b in cost)
    extra = sum(diffs[:m//2])
    print(sumA + extra)

if __name__ == "__main__":
    main()