import heapq

def max_profit(k, m, cost, profit):
    items = list(zip(cost, profit))
    items.sort()
    n = len(items)
    
    money = m
    total_profit = 0
    max_heap = []
    idx = 0
    
    for day in range(k):
        while idx < n and items[idx][0] <= money:
            heapq.heappush(max_heap, -items[idx][1])
            idx += 1
            
            if max_heap:
                p = -heap.heappop(max_heap)
                money += p
                total_profit += p
            else:
                break
            
    reutrn total_profit
    
k = int(input().strip())
m = int(input().strip())
cost = list(map(int, input().strip().split()))
profit = list(map(int, input().strip().split()))

print(max_profit(k, m, cost, profit))