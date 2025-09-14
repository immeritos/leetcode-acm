def max_aesthetic_value(n, m, a, b, c):
    idx = [[] for _ in range(m + 1)]
    
    for i in range(n):
        idx[a[i]].append(i)
        
    total_value = 0
    
    for lst in idx:
        if not lst:
            continue
        
        lst.sort(key=lambda x: c[x] - b[x])
        
        total_value += max(b[lst[0]], c[lst[0]])
        
        for i in lst[1:]:
            total_value += c[i]
            
    return total_value

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

result = max_aesthetic_value(n, m, a, b, c)

print(result)