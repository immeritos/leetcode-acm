"""
小华管理一个仓库,支持四种操作：

    in s:将编号为字符串 s(仅包含小写字母和数字,且各不相同）的产品入库。
    out:将最晚入库的产品出库,并输出其编号；若仓库空,输出 EMPTY。
    count;输出当前仓库中产品的数量。
    check;输出仓库中编号按字典序最小的产品;若仓库空,输出 EMPTY。

要求在 q<=2*10^5 次操作内高效完成上述四种操作。
"""
"""
输入：
13
check
in c1
in c2
count
check
in b3
in b4
count
check
out
check
out
check
"""
"""
输出：
EMPTY
2
c1
4
b3
b4
b3
b3
c1
"""

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