"""
在云化平台中, 组件按版本号统一管理, 版本号遵循语义化版本控制, 格式为：

major.minor.patch

    major: 重大更新, 可能包含向后不兼容的功能。
    minor: 在向后兼容的前提下新增功能。
    patch: 在向后兼容的前提下修复错误, 没有新增功能。

业务App在配置文件中声明其依赖组件及版本, 支持如下三种声明方式: 

    *: 取仓库中最新版本。
    ^major[.minor[.patch]]: 匹配相同major且版本号不低于声明版本的最大版本。
    -major.minor[.patch] 或 ~major.minor[.patch]: 匹配相同 major 和 minor 且版本号不低于声明版本的最大版本（即只更新补丁）。

    说明: - 与 ~ 前缀等价, 示例中使用 - 时也表示只更新补丁。

版本号缩写

声明时可省略 minor 或 patch, 未写出部分默认补齐为00, 例如: 

    2 等价于 2.0.0
    1.2 等价于 1.2.0


"""
"""
输入：
5
1.1.1
2.1
1.2.2
1.2.6
1.3.3
^1.2
"""
"""
输出：
1.3.3
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