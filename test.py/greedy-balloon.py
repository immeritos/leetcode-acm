def partition_balloon(s):
    last = {c: i for i, c in enumerate(s)}
    res = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            res.append(i - start + 1)
            start = i + 1
    return res

if __name__ == "__main__":
    s = input().strip()
    res = partition_balloon(s)
    print(res)