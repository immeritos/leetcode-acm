import sys
def main():
    w, h = map(int, input().split())
    m = int(input())
    k = int(input())
    
    cx = (w-1)/2
    cy = (h-1)/2
    
    pst = []
    
    matrix = [list(map(int, input().split())) for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            b = matrix[i][j]
            if b == m:
                d = abs(x - cx) + abs(y - cy)
                pts.append((d, i, j))
    
    pts.sort()
    
    res = pts[:min(k, len(pts))]
    out = []
    for _, x, y in res:
        out.append(f"{x} {y}")
    print(" ".join(out))
    
if __name__ == "__main__":
    main()