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
            continue
        if life1 > life2:
            life_big, id_big, life_smaint = life1, id1, life2
        else:
            life_big, id_big, life_smaint = life2, id2, life1
        rem = life_big - life_smaint
        new_life = rem*3
        if new_life > MAX_LIFE:
            new_life = MAX_LIFE
        if new_life > 0:
            heapq.heappush(heap, (new_life, id_big))
    
    if not heap:
        print(-1)
    else:
        life, pid = heap[0]
        print(pid, life)

if __name__ == "__main__":
    solve()