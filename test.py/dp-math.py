s = input().strip()
n = len(s)
a, b = map(int, input().split())

pref = [0] * (n+1)
for i in range(1, n+1):
    pref[i] = (pref[i-1] * 10 + int(s[i-1])) % a

suf = [0] * (n+1)
p = 1
for i in range(n-1, -1, -1):
    suf[i] = (int(s[i]) * p + suf[i+1]) % b
    p = (p * 10) % b
    
for i in range(n-1, 0, -1):
    if s[i] == '0':
        continue
    if pref[i] == 0 and suf[i] == 0:
        print("YES")
        print(s[:i])
        print(s[i:])
        break
else:
    print("NO")