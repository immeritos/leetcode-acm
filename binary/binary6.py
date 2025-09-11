def check(a, b, c, mid):
    a1, b1, c1 = a, b, c
    
    if a1 > mid:
        f = (a1 - mid) // x
        a1 -= x * f
        b1 += f
    
    if b1 > mid:
        f = (b1 - mid) // y 
        b1 -= y * f
        c1 += f
        
    return a1 >= mid and b1 >= mid and c1 >= mid

T = int(input())

for _ in range(T):
    a, b, c, x, y = map(int, input().split())
    
    l = 0
    r = 10**9
    
    while l < r:
        mid = (l + r + 1) // 2
        
        if check(a, b, c, mid):
            l = mid
        else:
            r = mid - 1
            
    print(l)