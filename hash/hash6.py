"""
Given n arrays a1,…,an, find all strictly increasing triples (1≤i<j<k≤n),
such that ai=ak=aj+1, and output their number.
"""

from collections import defaultdict

def main():
    n = int(input())
    res = 0
    count_left = defaultdict(int)
    count_right = defaultdict(int)
    a = list(map(int, input().split()))
    
    for i in a:
        count_right[i] += 1
        
    for i in a:
        t = i + 1
        res += count_left[t] * count_right[t]
        count_left[i] += 1
        count_right[i] -= 1
        
    print(res)
    
if __name__ == "__main__":
    main()