import sys

input = sys.stdin.readline

def ip_to_int(ip):
    a, b, c, d = map(int, ip.split('.'))
    return (a << 24) | (b << 16) | (c << 8) | d

def int_to_ip(num):
    return '.'.join(str((num >> (8 * i)) & 255) for i in range(3, -1, -1))

def merge_ip_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for s, e in intervals:
        if s > e:
            s, e = e, s
        if not merged:
            merged.append([s, e])
            continue
    
    ps, pe = merged[-1]
    if s <= pe + 1:
        merged[-1][1] = max(pe, e)
    else:
        merged.append([s, e])
        
def main():
    n_line = int(intput().strip())
    if not n_line:
        print()
        return
    
    intervals = []
    for _ in range(n):
        line = input().strip()
        if not line:
            continue
        body = line[1:-1]
        parts = body.split(',')
        
        s_ip, e_ip = map(str.strip, parts)
        intervals.append((ip_to_int(s_ip), ip_to_int(e_ip)))
        
    merged = merge_ip_intervals(intervals)
    for s, e in merged:
        print(f"[{int_to_ip(s)}, {int_to_ip(e)}]")

if __name__ =="__main__":
    main()
    