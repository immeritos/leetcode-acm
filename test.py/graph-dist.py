import sys
def main():
    N = int(input().strip())
    total = N + 1
    d = [list(map(int, input().split())) for _ in range(total)]
    m = int(input().strip())
    
    INF = 10**9
    dist = [INF]*total
    vis = [False]*total
    
    dist[0] = 0
    
    for _ in range(total):
        u = -1
        minDist = INF
        for i in range(total):
            if not vis[i] and dis[i] < minDist:
                u = i
                minDist = dist[i]
        if u == -1:
            break
        vis[u] = True
        for v in range(total):
            if not vis[v] and d[u][v] > 0 and dist[v] > dist[u] + dist[u][v]:
                dist[v] = dist[u] + d[u][v]
                
    print(dist[m])
    
if __name__ == "__main__":
    main()