import sys
import heapq

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    
    if not N:
        print("null")
        return 
    
    prio = {}
    pq = []
    buffer = []
    global_version = 0
    has_extract = False
    
    for _ in range(N):
        op = input().split()
        if not op:
            print("null")
            return
        if op[0] == "+":
            id_ = int(op[1])
            score = int(op[2])
            global_version += 1
            prio[id_] = (score, global_version)
            heapq.heappush(pq, (-score, id_, global_version))
        
        elif op[0] == "-":
            K = int(op[1])
            has_extract = True
            
            available = len(prio) - len(buffer)
            if K > available:
                print("-1")
                continue
            
            res = []
            while len(res) < K:
                if not pq:
                    print("null")
                    return
                score_neg, id_, ver = heapq.heappop(pq)
                s, v = prio.get(id_, (None, None))
                if v != ver:
                    continue
                res.append(id_)
                buffer.append((score_neg, id_, ver))
            print(" ").join(map(str, res))
            
        elif op[0] == "=":
            id_ = int(op[1])
            new_score = int(op[2])
            global_version += 1
            prio[id_] = (new_score, global_version)
            heapq.heappush(pq, (-new_score, id_, global_version))
            for node in buffer:
                heapq.heappush(pq,node)
            buffer.clear()
            
        else:
            print("null")
            return
    
    if not has_extract:
        print("null")
        return
    
if __name__ == "__main__":
    main()