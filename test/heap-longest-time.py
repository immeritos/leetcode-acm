"""
大模型训练通常采用数据并行的训练方式, 处理大规模数据集(样本), 加速训练过程, 具休的: 
假设有n个NPU, m个样本, 把m个样本分给n个NPU;
每个NPU上有一份完整模型, 各自计算自己的样本数据, 其中m>=n;
保证每个NPU至少分到一个样本, 且样本不能切分, 一个样本必须完整的被分到个NPU上;
每个NPU的运行时间跟所分到的样本的长度和呈正相关。
如果每个NPU上的样本长度和相差较大, 会形成木桶效应, 执行快的NPU等待执行慢的NPU, 最终执行时间由最大样本和长度的NPU决定。 
试着编号一段程序对样本进行均衡分配, 设n个NPU上分得的最大的样本和为l_max, 使l_max最小, 即求min(l_max)
"""
"""
输入：
4
7
89 245 64 128 79 166 144
"""
"""
输出：
245
"""

import sys
import heapq

def min_max_load(n, m, sample_lens):
    if m == 0 or n == 0:
        return 0

    # LPT：样本按长度降序    
    a = sorted(sample_lens, reverse=True)
    
    # 最小堆：每台 NPU 的当前负载    
    load = [0] * n
    heapq.heapify(load)

    l_max = 0
    for x in a:
        cur = heapq.heappop(load)   # 当前最空闲
        cur += x                    # 分配样本
        l_max = max(l_max, cur)     # 更新最大负载
        heapq.heappush(load, cur)
        
    return l_max

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    lens = list(map(int, input().strip().split()))
    
    # 若担心输入不足，可补齐/截断：lens = (lens + [0]*m)[:m]    
    print(min_max_load(n, m, lens))