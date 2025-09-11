import bisect

n, Q = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(Q):
    x = int(input())
    
    first = bisect.bisect_left(arr, x)
    last = bisect.bisect_right(arr, x) - 1
    
    if first < len(arr) and arr[first] == x:
        print(first + 1, last + 1)
    else:
        print(-1, -1)