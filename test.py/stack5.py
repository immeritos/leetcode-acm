import sys
import heapq

def main():
    input = sys.stdin.readline
    q = int(input())
    stack = []
    min_heap = []
    in_set = set()
    
    for _ in range(q):
        op = input().split()
        if op[0] == "in":
            s = op[1]
            stack.append(s)
            heapq.heappush(min_heap, s)
            in_set.add(s)
        elif op[0] == 'out':
            if not stack:
                print('EMPTY')
            else:
                s = stack.pop()
                in_set.remove(s)
                print(s)
        elif op[0] == 'count':
            print(len(in_set))
        elif op[0] == 'check':
            while min_heap and min_heap[0] not in in_set:
                heapq.heappop(min_heap)
            if not min_heap:
                print("EMPTY")
            else:
                print(min_heap[0])

if __name__ == "__main__":
    main()