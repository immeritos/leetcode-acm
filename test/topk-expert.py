"""
MOE 模型训练时, token 根据概率发送到 topk 个不同的专家进行计算。
这些专家分布在多个 NPU 卡上。路由算法将 token 的路由目标限制在 P 个 NPU 上, 可以有效降低通信成本。
具体的：
把 n 个专家平均分配在 m 个 NPU 上, 每个 NPU 上的专家为一个组;
设 n 个专家的编号为 N=[0,1,2,…,n-1] , 同一个专家组上的专家编号是连续的;
每个专家对应一个概率, 表示被路由到的可能性;
用每个组中的最大概率作为本组代表, 从所有组中选择概率最大的 p 个组, 其所在的 NPU 即为路由目标限制 NPU ;
再从上述 p 个 NPU 对应的所有专家概率中选择 k 个最大的概率对应的专家编号作为最终路由目标。
试着编写一段程序, 实现以上路由算法。
"""
"""
输入：
8 4 4 2
0.5 0.01 0.09 0.023 0.027 0.05 0.1 0.2
"""
"""
输出：
0 7
"""
import sys
import heapq
input = sys.stdin.readline

def solve():
    n, m, p, k = map(int, input().split())
    probs = [list(map(float, input().split())) for _ in range(n)]

    # 基本校验    
    if n<=0 or m<=0 or k<=0 or p<=0 or n & m != 0 or p>m:
        print("error")
        return
    
    g = n // m  # 每组专家数（连续编号）
    
    # Step 1：每组代表 = 组内最大概率（同概率取编号更小）
    # 用容量为 p 的小根堆保留“代表概率最大”的 p 个组
    grp_heap = []
    for gi in range(m):
        L, R = gi * g, (gi+1) * g
        # 代表索引：最大概率，平局取编号更小（用 -idx 打破平局）
        ridx = max(range(L, R), key=lambda idx: (probs[idx], -idx))
        rep = probs[ridx]
        heapq.heappush(grp_heap, (rep, -gi, gi))
        if len(grp_heap) > p:
            heapq.heappop(grp_heap)
            
    chosen_groups = [gi for _, __, gi in grp_heap]
    pool_size = g * len(chosen_groups)
    if k > pool_size:
        print("error")
        return
    
    exp_heap = []
    for gi in chosen_groups:
        L, R = gi * g, (gi+1) * g
        for idx in range(L, R):
            heapq.heappush(exp_heap, (probs[idx], -idx, idx))
            if len(exp_heap) > k:
                heapq.heappop(exp_heap)
    
    ans = sorted(idx for _, __, idx in exp_heap)
    print(" ".join(map(str, ans)))
    
if __name__ == "__main__":
    solve()