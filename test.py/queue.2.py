import sys
import heapq

def main():
    k, n = map(int, input().split())
    car_x, car_y = map(int, input().split())
    coords = [list(map(int, input().split())) for _ in range(n)]
    
    if k == 0 or k > n:
        print('null')
        return
    
    heap = []
    idx = 0
    for i in range(1, n+1):
        x, y = coords[idx][0], coords[idx][1]
        d = abs(car_x - x) + abs(car_y - y)
        idx += 2
        heapq.heappush(heap, (-d, -i, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    
    result = []
    while heap:
        d_neg, i_neg, x, y = heapq.heappop(heap)
        result.append((-d_neg, -i_neg, x, y))
    result.sort(key=lambda t: (t[0], t[1]))
    
    for d, i, x, y in result:
        print(i, x, y, d)
 
if __name__ == "__main__":
    main()