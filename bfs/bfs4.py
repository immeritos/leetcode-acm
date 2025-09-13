"""
Given an undirected graph stored as an adjacency list, use the breadth-first search (BFS) algorithm to calculate the number of connected patches in the graph.

In an undirected graph, a connected patch is the largest subgraph in which all nodes are connected by paths. 
You are required to output the number of connected patches in the graph.
"""

import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        
    def bfs(start):
        q = deque([start])
        visited[start] = True
        
        while q:
            node = q.popleft()
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)
    
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()