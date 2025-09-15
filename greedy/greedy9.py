def min_optimizers(pvs):
    n = len(pvs)
    covered = [False] * n
    has_opt = [False] * n
    ans = 0
    
    for i in range(n):
        if pvs[i] == i and not covered[i]:
            if i+1<n and p[i+1] == 0 and not has_opt[i+1]:
                has_opt[i+1] = True
                ans += 1
                covered[i] = True
                if i+2 < n and pvs[i+2] == 1:
                    covered[i+2] = True
            elif i-1>=0 and pvs[i-1] == 0 and not has_opt[i-1]:
                has_opt[i-1] = True
                ans += 1
                covered[i] = True
                if i-2 >= 0 and pvs[i-2] == 1:
                    covered[i-2] = True
            else:
                return -1
    return ans

if __name__ == "__main__":
    N = int(input().strip())
    pvs = list(map(int, input().split()))
    print(min_optimizers(pvs))