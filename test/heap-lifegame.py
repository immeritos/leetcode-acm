"""
该问题要求模拟一系列“玩家1对1对战”的过程, 每轮选择当前生命值最小且不为0的两名玩家进行PK, 直到无法匹配出两名玩家或所有玩家生命值归零。
如果在挑选符合PK条件的2个玩家过程中, 能量值相同的候选玩家有多个时, 则挑选玩家编号小的玩家参与PK;
如是2个玩家的生命能量值相同, 则2个玩家同归于尽, 生命能量值都归为0,PK后都退出游戏;
如果2个玩家的生命能量值不同, 则能量值大的玩家胜出, PK过程胜出玩家会消耗掉另一个玩家的同等数量的生命能量值;
PK胜出后, 则剩余生命能量值会膨胀3倍(最大不超过32位有符号整数的最大值), 即该玩家最终的生命能量值为剩余能量值的3倍。
PK胜出的玩家仍可继续游戏.
"""
"""
输入样例：
4
2 5 1 8
"""
"""
输出样例：
4 6
"""

import sys
import heapq

MAX_LIFE = 2**31 - 1

def solve():
    input = sys.stdin.readline
    
    n = int(input().strip())
    lives = list(map(int, input().split()))
    
    heap = []
    for i, v in enumerate(lives, start=1):
        if v > 0:
            heapq.heappush(heap, (v, i))
    
    while len(heap) >= 2:
        life1, id1 = heapq.heappop(heap)
        life2, id2 = heapq.heappop(heap)
        if life1 == life2:
            # 同归于尽：两人都不再入堆
            continue
        # 生命值不同：较大值胜
        if life1 > life2:
            life_big, id_big, life_small = life1, id1, life2
        else:
            life_big, id_big, life_small = life2, id2, life1
        # 扣除与膨胀
        rem = life_big - life_small
        new_life = rem*3
        if new_life > MAX_LIFE:
            new_life = MAX_LIFE
            
        heapq.heappush(heap, (new_life, id_big))
    
    if not heap:
        print(-1)
    else:
        life, pid = heap[0]
        print(pid, life)

if __name__ == "__main__":
    solve()