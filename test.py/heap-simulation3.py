"""
云化平台对于组件按版本号进行统一管理，版本号遵循语义版本控制系统,格式为:

major.minor.patch

其中

major: 项目进行重大更新，且包含不向后兼容的功能

minor:仅在以向后兼容的方式添加新功能

patch:仅在以向后兼容的方式修复错误，并且没有添加任何新的功能

业务App在其配置文件中声明其依赖的组件及版本, 如:1.1.0

并且版本号可以缩写, 没有写出来的部分表示为0
"""
"""
"""
"""
"""

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