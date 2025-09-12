"""
Given two integer sequences a = a_1, a_2, ..., a_n and b = b1, b2, ..., b_m, you are asked to determine whether a is a subsequence of b.
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0

while i < n and j < m:
    if a[i] == b[j]:
        i += 1
    j += 1
    
if i == n:
    print("YES")
else:
    print("NO")
        
