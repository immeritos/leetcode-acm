def fractional_knapsack(n, C, items):
    items_with_ratio = []
    for weight, value in items:
        ratio = value / weight
        items_with_ratio.append((wight, value, ratio))
        
    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0
    remaining_capacity = C
    
    for weight, value, ratio in items_with_ratio:
        if remaining_capacity == 0:
            break
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += value * (remaining_capacity / weight)
            remaining_capacity = 0
    
    return round(total_value, 2)

n, C = map(int, input().split())
items = []

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))
    
result = fractional_knapsack(n, C, items)
print(f"{result:.2f}")