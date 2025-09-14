import sys
sys.setrecursionlimit(1_000_000)

n_and_rest = sys.stdin.read().split()
n = int(n_and_rest[0])
h = list(map(int, n_and_rest[1:n+1]))
h = [0] + h

def min_cost(l, r):
    if l > r:
        return 0
    if l == r:
        return 2
    min_h = min(h[l:r+1])
    cost1 = 1
    i = l
    while i <= r:
        if h[i] > min_h:
            start = i
            while i <= r and h[i] > min_h:
                i += 1
            cost1 += min_cost(start, i - 1)
        else:
            i += 1
    return cost1

total_min_cost = min_cost(1, n)
print(total_min_cost)