"""
Given an undirected graph, where each node is numbered with an integer and the graph is stored as an adjacency list, calculate the number of connected patches in the graph. 
We define a connected patch as a maximal subgraph of the graph in which any two nodes are connected by a path. 
In other words, a connected patch is a connected portion of the undirected graph in which any two nodes are connected by a set of edges.
"""
import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

            
def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)
        
    for i in range(1, n + 1):
        adj[i].sort()

    def dfs(node):
        visited[node] = True
        for neighbour in adj[node]:
            if not visited[neighbour]:
                dfs(neighbour)
                        
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1
    
    print(count)
    
if __name__ == "__main__":
    main()