"""
Given a directed acyclic graph, with nodes numbered from 1 to n, the edges are directed, each consisting of a start and an end point. 
In graph theory, a directed graph is a directed acyclic graph (DAG) if it is impossible to return from a vertex via several edges. The graph is stored using an adjacency list; for each node uu, all its outgoing edges are stored in a list. 
Find the number of unique paths from node s to node t.
"""

import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        if u == v:
            continue
        adj[u].append(v)
        
    s, t = map(int, input().split())

    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dfs(node):
        if node == t:
            return 1
        total = 0
        for neighbour in adj[node]:
            total += dfs(neighbour)
        return total

    ans = dfs(s)
    print(ans)
    
if __name__ == "__main__":
    main()