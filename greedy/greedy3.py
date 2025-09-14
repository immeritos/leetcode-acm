def max_activites(n, activities):
    activities.sort(key:lambda x: x[1])
    
    count = 0
    last_end_time = -1
    
    for start, end in activities:
        if start > last_end_time:
            count += 1
            last_end_time = end
            
    return count

n = int(input())
activities = []
for _ in range(n):
    start, end = map(int, input().split())
    activities.append((start, end))
    
print(max_activites(n, activities))