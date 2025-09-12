MAX = 1001
adj = [[] for _ in range(MAX)]
visited = [False] * MAX

def dfs(node):
    visited[node] = True
    for neighbour in adj[node]:
        if not visited[neighbour]:
            dfs(neighbour)
            
def main():
    n, m = map(int, input().split())
    
    for i in range(1, n+1):
        visited[i] = False
        adj[i] = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        if u != v:
            adj[u].append(v)
            adj[v].append(u)
            
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1
    
    print(count)
    
if __name__ == "__main__":
    main()