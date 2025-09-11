"""
Given an array a of length n and Q queries. Each query consists of a number x and an integer k. 
For each query, find the position of the k-th occurrence of the number x in the array (starting at 1). 
If x appears fewer than k times in the array, output -1.
"""

from collections import defaultdict

def main():
    n, Q = map(int, input().split())
    
    a = list(map(int, input().split()))
    
    positions = defaultdict(list)
    for i in range(n):
        positions[a[i]].append(i+1)
        
    for _ in range(Q):
        x, k = map(int, input().split())
        
        if len(positions[x]) < k:
            print(-1)
        else:
            print(positions[x][k-1])

if __name__ == "__main__":
    main()