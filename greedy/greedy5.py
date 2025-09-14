def min_groups(n, k, a):
    group_count = 1
    min_val = a[0]
    max_val = a[0]
    
    for i in range(1, n):
        if a[i] - min_val > k or max_val - a[i] > k:
            group_count += 1
            min_val = a[i]
            max_val = a[i]
        else:
            min_val = min(min_val, a[i])
            max_val = max(max_val, a[i])
            
    return group_count

n, k = map(int, input().split())
a = list(map(int, input().split()))

print(min_groups(n, k, a))