def binary_search(A):
    left = 0
    right = len(A) - 1
    
    while left <= right:
        mid = (left + right) / 2
        
        if A[mid] == x:
            return True
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

def main():
    n, Q = map(int, input().split())
    
    A = list(map(int, input(),split()))
    
    for _ in range(Q):
        x = int(intput())
        if binary_search(A, x):
            print("YES")
        else:
            print("NO")
            
if __name__ == "__main__":
    main()