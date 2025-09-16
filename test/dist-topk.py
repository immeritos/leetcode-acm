"""
给定一张二维图像, 图像中每个值表示该坐标下的亮度。
现在给定一个亮度值 m , 请返回离图像中心坐标最近的 k 个亮度为 m 值的坐标 (x, y)。

提示：

1.图像中元素的坐标范围 x:[0,w-1], y:[0,h-1] 。

2.图像宽高 w,h 均为奇数, 图像中心坐标 (w-1)/2,(h-1)/2 。

3.平面上两点之间的距离为 |x1-x2|+|y1-y2| 。

4.在距离相同的情况下, 以 x 小的点优先；当 x 相同时, 以 y 小的点优先。

5.题目可保证至少存在一个亮度值为 m 的点。
"""
"""
输入：
5 5
10
3
10 2 3 4 5
1 2 3 4 10
1 2 3 10 5
1 10 3 4 5
1 2 3 4 5
"""
"""
输出：
3 2 1 3 4 1
"""

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