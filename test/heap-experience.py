"""
有一个经验池，需要支持三种操作，共有 N 次操作：

    插入经验
    格式：+ id score
    向池中插入一个编号为 id 的经验，初始优先级为 score。

    提取 TopK 经验
    格式：- K
    从当前经验池中提取优先级最高的 K 个经验的 id(按优先级降序，如果优先级相同按 id 升序）;
    提取后，这些经验暂时从池中移除。如果此时池中剩余经验不足 K 个，则输出 -1。

    更新优先级
    格式：= id newScore
    将编号为 id 的经验的优先级更新为 newScore; 更新后，之前所有被提取(但尚未真正“消耗”）的经验都要重新回到池中，且优先级为最新值。

若所有操作中没有任何一次提取操作，则输出 null。若输入行数与 N 不符，也输出 null。
"""
"""
输入：
7
+ 1 5
+ 2 10
+ 3 7
- 2
= 3 20
- 1
- 1
"""
"""
输出：
2 3
3
2
"""
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