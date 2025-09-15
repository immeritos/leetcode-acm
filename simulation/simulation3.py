import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    tests = []
    index = 0
    for i in range(n):
        mask = 0
        for j in range(m):
            x = int(input().split()[index])
            index += 1
            if x == 1:
                mask |= (1 << j)
        tests.append(mask)
        
    target = (1 << m) - 1
    ans = float('inf')
    
    for s in range(1 << n):
        union_mask = 0
        cnt = 0
        for i in range(n):
            if s & (1 << i):
                union_mask |= tests[i]
                cnt += 1
        if union_mask == target:
            ans = min(ans, cnt)
    
    print(-1 if ans == float('inf') else ans)

if __name__ == "__main__":
    main()           