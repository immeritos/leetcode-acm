"""
Given an integer array arr, you need to process multiple queries. Each query contains a range [l,r], 
and you need to find the maximum value in the range and all indexes where the maximum value occurs.
"""

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        
        max_value = arr[l]
        max_indices = [l+1]
        
        for i in range(l+1, r+1):
            if arr[i] > max_value:
                max_value = arr[i]
                max_indices = [i+1]
            elif arr[i] == max_value:
                max_indices.append(i+1)
                
        print(max_value)
        print(' '.join(map(str, max_indices)))
        
if __name__ == "__main__":
    main()