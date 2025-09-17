"""
一个超大智能汽车测试场有多个充电桩，每个充电桩的位置由其在二维平面上的坐标 (x,y) 表示。
给定一辆智能汽车的当前位置 (car_x,car_y) ，请设计一个高效的算法，找出给定智能汽车行驶到充电桩行驶距离最近的 k 个充电桩井输出相关充电桩信息(编号、坐标、行驶距离)，且按行驶距离升序排序(最近行驶距离的排在最前面)，如果存在行驶距离相等的充电桩则按照充电桩的编号从小到大输出。
汽车到充电桩的行驶距离的计算方法为 abs(car_x-x)+abs(car_y-y)
"""
"""
输入：
3 5
0 0
1 4
5 6
2 3
7 8
3 -1
"""
"""
输出：
5 3 -1 4
1 1 4 5
3 2 3 5
"""

import sys
import heapq
input = sys.stdin.readline

def main():
    k, n = map(int, input().split())
    car_x, car_y = map(int, input().split())
    coords = [list(map(int, input().split())) for _ in range(n)]
    
    if k == 0 :
        print('null')
        return
    if k > n:
        print("null")
        return

    # 维护大小为 k 的“最大堆”：用 (-distance, -id) 模拟    
    heap = []
    for i, (x, y) in enumerate(coords, start=1):
        d = abs(car_x - x) + abs(car_y - y)
        # 压入 (负距离, 负编号, x, y)
        heapq.heappush(heap, (-d, -i, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    
    result = []
    while heap:
        d_neg, i_neg, x, y = heapq.heappop(heap)
        result.append((-d_neg, -i_neg, x, y))
    result.sort(key=lambda t: (t[0], t[1]))  # 距离、编号 升序
    
    for d, i, x, y in result:
        print(i, x, y, d)
 
if __name__ == "__main__":
    main()