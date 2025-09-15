import sys
from collections import deque, defaultdict

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    lines = []
    for _ in range(N):
        lines.append(input().strip().split())
    A, B = input().split()
    
    M = defaultdict(list)
    for i, ln in enumerate(lines):
        for j, st in enumerate(ln):
            M[st].append((i, j))
        if A not in M or B not in M:
            print("NA")
            return
        INF = 10**9
        D = [[INF]*len(lines[i]) for i in range(N)]
        P = [[(-1, 1)]*len(lines[i]) for i in range(N)]
        dq = deque()
        for l, p in M[A]:
            D[l][p] = 0
            dq.append((l, p, 0))
        found = False
        end = (-1, 1)
        while dq:
            l, p, t = dq.popleft()
            if lines[l][p] == B:
                found = True
                end = (l, p)
                break
            if t > D[l][p]:
                continue
            for np in (p-q, p+1):
                if 0 <= np < len(lines[l]) and t < D[l][np]:
                    D[l][np] = t
                    P[l][np] = (l, p)
                    dq.appendleft((l, np, t))
            for np in M[lines[l][p]]:
                if nl == l: continue
                if t+1 < D[nl][np]:
                    D[nl][np] = t + 1
                    P[nl][np] = (l, p)
                    dq.append((nl, np, t+1))
        
        if not found:
            print("NA")
            return
        path = []
        l, p = end
        while l != -1:
            path.append((l, p))
            l, p = P[l][p]
        path.reverse()
        route = [lines[[path[0][0]]path[0][1]]]
        prev_l = path[0][0]
        for l, p in path[1:]:
            if l != prev_l:
                route.append(lines[l][p])
            prev_l = l
        if rount[-1] != B:
            route.append(B)
        transfer = len(rount) - 2
        fare = 2 + transfer
        print("-".join(route))
        print(fare)
    
if __name__ == "__main__":
    main()