import sys
sys.setrecursionlimit(1_000_000)

def main():
    input = sys.stdin.readline
    n, m, s, t = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for eid in range(1, m+1):
        u, v = map(int, input().split())
        adj[u].append((v, eid))
        adj[v].append((u, eid))
    for u in range(1, n+1):
        adj[u].sort(key=lambda x: x[1])
    
    visited = [False] * (n+1)
    path_edges = []
    edge_paths = [[] for _ in range(m+1)]
    pid = 0
    
    def dfs(u):
        nonlocal pid
        if u == t:
            pid += 1
            for e in path_edges:
                edge_paths[e].append(pid)
            return
        for v, eid in adj[u]:
            visited[v] = True
            path_edges.append(eid)
            dfs(v)
            path_edges.pop()
            visited[v] = False
            
    visited[s] = True
    dfs(s)
    
    q = int(input())
    for _ in range(q):
        eid = int(input())
        vec = edge_paths[eid]
        print(len(vec), *vec)
        
if __name__ == "__main__":
    main()