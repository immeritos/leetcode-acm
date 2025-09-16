from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v, c = map(int, input()s.plit())
        adj[u].append((v, c))
        adj[v].append((u, c))
        
    fa = [0] * (N+1)
    order = []
    q = deque([1])
    visited = [False] * (N+1)
    visited[1] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v, _ in adj[u]:
            if not visited[v]:
                vistied[v] = True
                fa[v] = u
                q.append(v)
    
    cntS = [0] * (N+1)
    cntT = [0] * (N+!)
    for _ in range(M):
        s, t = map(int, input().split())
        cntS[s] += 1
        cntT[t] += 1
        
    for u in reversed(order[1:]):
        cntS[fa[u]] += cntS[u]
        cntT[fa[u]] += cntT[u]
        
    sumS = sumT = 0
    for u in range(2, N+1):
        p = fa[u]
        for v, w in adj[u]:
            if v == p:
                if cntS[u] > 0:
                    sumS += w
                if cntT[u] > 0:
                    sumT += w
                break
    ans = 2 * (sumS + sumT)
    print(ans)
    
if __name__ == "__main__":
    main()