"""
快过年了，小明想要用工作攒下的钱 m 做一点生意补贴家用。
和小卖部老板达成协商，可以按成本价格给他提供 n 种商品，让他到隔壁村去销售，
其中商品 i 的成本价为 cost[i]; 利润为 profit[i].

由于小明没法携带太多商品，老板也不想在过年期间工作，所以小明每天最多能从老板那里进 1 次货，每次买 1 件商品，购买后的商品无法再次购买。

老板不接收赊账，每种商品只有 1 件库存，请问小明在 k 天中最多可以赚多少利润呢?
"""
"""
输入：
3
2
2 5 7
2 5 7
"""
"""
输出：
2
"""

import sys
import heapq

input = sys.stdin.readline

def max_profit(k, m, cost, profit):
    items = sorted(zip(cost, profit), key=lambda x: x[0])
    n = len(items)
    
    money = m
    total = 0
    max_heap = []
    i = 0
    
    for _ in range(k):
        # 把当前资金能买的都放进堆（按利润）
        while i < n and items[i][0] <= money:
            heapq.heappush(max_heap, -items[i][1])
            i += 1
            
            if not max_heap:  # 没东西可以买了
                break

            # 选择利润最大的一个
            p = -heapq.heappop(max_heap)
            money += p
            total += p
            
    return total

if __name__ == "__main__":

    k = int(input().strip())
    m = int(input().strip())
    cost = list(map(int, input().strip().split()))
    profit = list(map(int, input().strip().split()))

    print(max_profit(k, m, cost, profit))