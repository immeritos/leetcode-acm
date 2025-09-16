import sys

def parse(s):
    parts = s.split('.')
    return tuple(int(parts[i]) if i < len(parts) else 0 for i in range(3))

def format_version(v):
    major, minor, patch = v
    if patch == 0:
        if minor == 0:
            return f"{major}"
        return f"{major}.{minor}"
    return f"{major}.{minor}.{patch}"

N = int(input())
versions = [parse(input().strip()) for _ in range(N)]
req = input().strip()

best = (-1, -1, -1)

def at_least(v, target):
    return v >= target

if req == "*":
    best = max(versions)
else:
    mode = req[0]
    target = parse(req[1:])
    for v in versions:
        if mode == '^':
            if v[0] != target[0] or not at_least(v, target):
                continue
        if mode in ('-', '~'):
            if v[0] != target[0] or v[1] != target[1] or not at_least(v, target):
                continue
        if v > best:
            best = v

if best[0] < 0:
    print('None')
else:
    print(format_version(best))