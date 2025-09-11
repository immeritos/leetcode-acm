"""
Given an array a of length n, where each element is a positive integer, 
we need to answer n queries, where the i-th query is about a prefix a_1, a_2, ..., a_i of the array:
For each query i, count how many times the number i appears in the prefix a_1, a_2, ..., a_i
"""

n = int(input())
a = list(map(int, input().split()))

counts = {i : 0 for i in range(1, n+1)}

for i in range(n):
    num = a[i]
    counts[num] += 1
    if i > 0:
        print(' ', end='')
    print(counts[i+1], end='')
    
print()