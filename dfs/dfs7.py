import sys
sys.setrecursionlimit(20000)

def dfs(node, father, adj, a):
    total_add = 0
    total_sum = 0
    
    for neighbour in adj[node]:
        if neighbour != father:
            child_add, child_sum = dfs(neighbour, node, adj, a)
            total_add += child_add
            total_sum += child_sum
            
    if a[node] < total_sum:
        total_add += total_sum - a[node]
        a[node] = total_sum
        
    return total_add, a[node]

def solve(n, a, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    result, _ = dfs(0, -1, adj, a)
    return result

n = int(input())
a = list(map(int, input().split()))
edges = [tuple(map(int, input().split()))]

print(solve(n, a, edges))