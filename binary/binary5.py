R = list(map(int, input().split()))
cnt = int(input())

def check(i):
    su = 0
    for x in R:
        su += min(i, x)
    return su <= cnt 

l, r = 0, 10**9
while l <= r:
    mid = l + r / 2
    if check(mid):
        l = mid + 1
    else r = mid - 1

if r == 10**9:
    r = -1
print(r)