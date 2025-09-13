"""
Given a tree with n nodes, numbered 1-n, and with the root node fixed at 1, there are two ways to represent the tree structure:

Method 1: Use n-1 edges, where each edge u v represents an edge between nodes u and v.
Method 2: Use an array of parents, where parent[i] represents the parent of node i+1.

Write a program that reads the tree structure and uses a depth-first search to traverse it and print the node numbers.
"""
import syssys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def dfs(node, par=-1):
    traversal.append(node)
    for nxt in adj[node]:
        if nxt != par:
            dfs(nxt, node)
            
n = int(input().strip())
tree_type = int(input().strip())

adj = [[] for _ in range(n+1)]
traversal = []

if tree_type == 1:
    for _ in range(n-1):
        u, v =  map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
elif tree_type == 2:
    parents = list(map(int, input().split()))
    for i in range(1, n + 1):
        p = parents[i - 1]
        if p != 0:
            adj[p].append(i)
            adj[i].append(p)
        
for i in range(1, n+1):
    adj[i].sort()
    
dfs(1, 0)

print(" ".join(map(str, traversal)))