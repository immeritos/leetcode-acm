"""
Tazi has a tree of n nodes, with node 1 being the root. Each node has a weight, ai. 
If the weight of any node is greater than or equal to the sum of the weights of its children, then the tree is a magical tree. 
During each operation, Tazi selects a node and increases its weight by one. 
What is the minimum number of operations Tazi needs to perform to transform this tree into a magical tree?
"""

import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    a = [0] + arr
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    def dfs(u, p):
        ops_u = 0
        children_sum = 0
        for v in adj[u]:
            if v == p:
                continue
            ops_v, val_v = dfs(v, u)
            ops_u += ops_v
            children_sum += val_v
        
        if a[u] < children_sum:
            deficit = children_sum - a[u]
            ops_u += deficit
            val_u = children_sum
        else:
            val_u = a[u]
            
        return ops_u, val_u        
        
    ops, _ = dfs(1, 0)
    print(ops)

if __name__ == "__main__":
    main()