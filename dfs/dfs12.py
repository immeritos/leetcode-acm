import sys
sys.setrecursionlimit(1_000_000)

def dfs(i, f):
    global ans
    if i >= n or a[i] == 0:
        return
    cur = (a[i] - 1 + f) % 3
    need = (b[i] - 1 - cur + 3) % 3
    nf = (f + need) % 3
    dfs(2*i + 1, nf)
    dfs(2*i + 2, nf)

def main():
    global n, a, b, s
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print(ans)
    
if __name__ == "__main":
    main()