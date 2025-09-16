"""
给定一个长度可达1000位的非负整数字符串s,以及两个正整数a和b, 要求将s从某个位置切割成两部分, 使得:

    切割后得到的左半部分和右半部分均为正整数, 且不含前导零;
    左半部分能够被a整除;
    右半部分能够被b整除。

如果存在多种切割方式, 需返回使得左半部分数值最大的那一种；若无法切割则输出 NO。
"""
"""
输入：
116401024
97 1024
"""
"""
输出：
YES
11640
1024
"""

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