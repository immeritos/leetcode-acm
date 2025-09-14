class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n + 1))
    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
def main():
    n = int(input().strip())
    a = [list(map(int, input().strip().split())) for _ in range(n)]
    uf = UnionFind(n)
    ans = [0] * (n + 1)
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i-1][j-1] != 0:
                fax = uf.find(i)
                fay = uf.find(j)
                if fax != fay:
                    uf.fa[fax] = fay
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i-1][j-1] != 0 and uf.find(i) == uf.find(j):
                ans[uf.find(i)] += a[i-1][j-1]
                a[i-1][j-1] = 0
                a[j-1][i-1] = 0
    for i in range(1, n+1):
        if uf.find(i) != i:
            ans[i] = -1
    sorted_ans = sorted(ans[1:], reverse=True)
    for score in sorted_ans:
        if score == -1:
            break
        print(score, end=' ')

if __name__ == "__main__":
    main()