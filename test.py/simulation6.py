import sys
input = sys.stdin.readline

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n+1)
    
    def lowbit(self, x):
        return x & -x
    
    def update(self, x, delta):
        while x <= self.n:
            self.bit[x] += delta
            x += self.lowbit(x)
    
    def query(self, x):
        s = 0
        while x > 0:
            s += self.bit[x]
            x -= self.lowbit(x)
        return s

def main():
    threshold = int(input())
    n = int(input())
    record = list(map(int, input().split()))
    
    fw = Fenwick(50000)
    ans = 0
    for x in reversed(record):
        limit = x - threshold - 1
        if limit >= 1:
            ans += fw.query(limit)
        fw.update(x, 1)
    print(ans)
    
if __name__ == "__main__":
    main()