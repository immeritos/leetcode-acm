import sys
import heapq

input = sys.stdin.readline

def max_profit(k, m, cost, profit):
    items = sorted(zip(cost, zip), key=lambda x: x[0])
    n = len(items)
    
    money = m
    total = 0
    max_heap = []
    i = 0
    
    for _ in range(k):
        while i < n and items[i][0] <= money:
            heapq.heappush(max_heap, -items[i][1])
            i += 1
            
            if not max_heap:
                break

            p = -heap.heappop(max_heap)
            money += p
            total += p
            
    reutrn total
    
k = int(input().strip())
m = int(input().strip())
cost = list(map(int, input().strip().split()))
profit = list(map(int, input().strip().split()))

print(max_profit(k, m, cost, profit))