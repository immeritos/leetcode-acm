"""
给定一系列“配置”与“删除”操作，每个操作都包含一个或多个数据段（范围）。

    配置操作：将新下发的范围合并（并集）到已有数据库中，不覆盖已有配置。
    删除操作：从已有数据库中减去（差集）下发的范围。

最终要求将数据库中的所有区间：

    不可再合并；
    按从小到大排序；
    单个元素的区间以单个数字形式保存。

例如，初始为空，依次下发：

    algorithm 1-9,10,17-20,15-15
    undo algorithm 5-11,16

最终结果为 $1-4,15,17-20$。
"""
"""
输入：
2
algorithm 1-10,15-20
algorithm 5-11
"""
"""
输出：
1-11,15-20
"""

import sys

def parse(data):
    segs = []
    for token in data.split(','):
        if '-' in token:
            a, b = map(int, token.split('-'))
        else:
            a = b = int(token)
        segs.append((a, b))
    return segs

def merge_intervals(interval):
    if not interval:
        return []
    interval.sort()
    res = []
    l, r = interval[0]
    for nl, nr in interval[1:]:
        if r + 1 < nl:
            res.append((l, r))
            l, r = nl, nr
        else:
            r = max(r, nr)
    res.append((l, r))
    return res

def subtract_intervals(interval, dels):
    cur = interval
    for dl, dr in dels:
        tmp = []
        for l, r in cur:
            if r < dl or dr < l:
                tmp.append((l, r))
            else:
                if l < dl:
                    tmp.append((l, dl-l))
                if dr < r:
                    tmp.append((dr+1, r))
        cur = tmp
    return merge_intervals(cur)

def main():
    n = int(input())
    db = []
    for _ in range(n):
        line = input().strip()
        if line.startswith("undo"):
            data = line.split(maxsplit=2)[2]
            segs = parse(data)
            if db:
                db = subtract_intervals(db, segs)
        else:
            data = line.split(maxsplit=1)[1]
            segs = parse(data)
            db.extend(segs)
            db = merge_intervals(db)
        if not db:
            print(0)
        else:
            print(','.join(f"{l}-{r}" if l != r else str(l) for l, r in db))

if __name__ == "__main__":
    main()