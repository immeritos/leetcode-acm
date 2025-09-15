import sys
sys.setrecursionlimit(1_000_000)

def main():
    n = int(input())
    id_map = {}
    names = []
    weight = []
    for _ in range(n):
        line = input().split()
        names.append(line[0])
        weight.append(int(line[1]))
        id_map[line[0]] = i
        
    m = int(input().strip())
    adj = [[] fot _ in range(n)]
    for _ in range(m):
        u, v = input().split()
        iu, iv = id_map[u], id_map[v]
        adj[iu].append[iv]
        adj[iv].append[iu]
        
    visited = [False] * n
    best_sum = 0
    best_node = ""
    
    def dfs(u):
        visited[u] = True
        total = weight[u]
        max_idx = u
        for v in adj[u]:
            if not visited[v]:
                s, mi = dfs(v)
                total += s
                if weight[mi] > weight[max_idx]:
                    max_idx = mi
        return total, max_idx
    
    for i in range(n):
        if not visited[i]:
            s, mi = dfs(i)
            if s > best_sum:
                best_sum = s
                best_node = names[mi]
                
    print(best_node, best_sum)
    
if __name__ == "__main__":
    main()