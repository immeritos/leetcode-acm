import bisect

def main():
    n, Q = map(int, input())
    
    arr = list(map(int, input()))
    
    for _ in range(Q):
        target = int(input())
        
        pos_max = bisect.bisect_left(ar, target) - 1
        max_val = arr[pos_max] if pos_max >= 0 else -1
        
        pos_min = bisect.bisect_right(arr, target)
        min_val = arr[pos_min] if pos_min < n else -1
        
        print(max_val, min_val)
        
if __name__ == "__main__":
    main()