"""
Xiaohong has a permutation p of length n. 
She wants to know how many (i, j) pairs in p satisfy: 
i < j and p_i + p_j = i + j.

Please help her calculate this.
"""

def count_pairs(n, p):
    diff_count = {}
    result = 0
    
    for j in range(n):
        diff = (j+1) - p[j]
        
        if -diff in diff_count:
            result += diff_count[-diff]
            
        if diff in diff_count:
            diff_count[diff] += 1
        else:
            diff_count[diff] = 1
    
    return result

n = int(input())
p = list(map(int, input().split()))

print(count_pairs(n, p))