from collections import defaultdict

def main():
    n, m = map(int, input().split())
    
    g = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        
    s, t = map(int, input().split())
    
    def dfs(u):
        if u == t:
            return 1
        
        res = 0
        
        for v in g[u]:
            res += dfs(v)
        
        return res
    
    ans = dfs(s)
    
    print(ans)
    
if __name__ == "__main__":
    main()