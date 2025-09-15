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
            data = line.splits(maxsplit=2)[2]
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