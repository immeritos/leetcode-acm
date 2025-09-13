"""
Tazi has a tree with n nodes, the root node is node 1, and each node of the tree is red or black. 
She wants to know how many nodes have subtrees that contain both red and black dots.
"""

import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def main():
    n = int(input().strip())
    color = input().strip()
    
    adj = [[] for _ in range(n+1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        
    ans = 0
    
    def dfs(node, par):
        nonlocal ans
        has_red = (color[node - 1] == 'R')
        has_black = not has_red
        
        for neighbour in adj[node]:
            if neighbour == par:
                continue
            r, b = dfs(neighbour, node)
            has_red |= r
            has_black |= b
        
        if has_red and has_black:
            ans += 1
        return has_red, has_black
    
    dfs(1, 0)
    print(ans)
    
if __name__ == "__main__":
    main()