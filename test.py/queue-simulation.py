import sys
import heapq

def main():
    pq = []
    order = 0
    ops = []
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        parts = line.split()
        ops.append(parts)
        
    last_run = max(i for i, op in enumerate(ops) if op[0] == "run")
    
    for i, op in enumerate(ops):
        if op[0] == "add":
            _, tid, p, t = op
            heapq.heappush(pq, (int(p), order, int(tid), int(t)))
            order += 1
        else:
            T = int(op[1])
            while T > 0 and pq:
                p, ord_v, tid, rem = heapq.heappop(pq)
                if rem <= T:
                    T -= rem
                else:
                    rem -= T
                    T = 0
                    heapq.heappush(pq, (p, ord_v, tid, rem))
            if i == last_run:
                if not pq:
                    print("idle")
                else:
                    print(pq[0][2])

if __name__ == "__main__":
    main()