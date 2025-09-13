"""
Tazi has a complete binary tree with n nodes. 
The definition of a complete binary tree is: each node either has two children or no children.

A node with no children has a weight of 1.

A node with two children has a weight equal to the product of the weights of its two children.

Each node has two operations: addition or multiplication. Given an array c of length n, as shown below.

ci=0 indicates that the operation on node i is addition, and ci=1 indicates that the operation on node i is multiplication.

Now, Tazi asks you what the weight of the root node of this complete binary tree is.
"""
import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

MOD = 10**9 + 7

def main():
    n = int(input().strip())
    
    parents = list(map(int, input().split()))
    ops = list(map(int, input().split()))
    
    adj = [[] for i in range(n + 1)]
    for i in range(2, n + 1):
        p = parents[i-2]
        adj[p].append(i)
        
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def cal(u):
        if not adj[u]:
            return 1
        
        a = cal(adj[u][0])
        b = cal(adj[u][1])
        if ops[u] == 0:
            return (a + b) % MOD
        if ops[u] == 1:
            return (a * b) % MOD
        
    print(cal(0))
    
if __name__ == "__main__":
    main()