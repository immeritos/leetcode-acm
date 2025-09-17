"""
设计一个简单的任务调度器, 支持两种操作：

    添加任务：格式为 add task_id priority time

    task_id∈[0,65535]：任务唯一标识
    priority∈[0,99]：优先级, 数值越小优先级越高
    time∈[1,10000]：需要的时间片数量

运行调度：格式为 run T

    消耗 T∈[1,100000] 个时间片, 调度器每次选取当前队列中优先级最低的任务执行, 执行过程中如果有新任务加入且比当前运行任务优先级更高, 则会抢占。
    仅在 最后一次 run 操作完成后, 输出此时正在调度的任务 ID, 若无任务则输出 idle。

"""
"""
输入：
add 101 0 10
add 20 1 3
add 300 0 1
run 11
"""
"""
输出：
20
"""

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
                # 任务完成，不再入堆
                if rem <= T:
                    T -= rem
                # 任务未完成，重新入堆
                else:
                    rem -= T
                    T = 0
                    heapq.heappush(pq, (p, ord_v, tid, rem))
            if i == last_run:
                if not pq:
                    print("idle")
                else:
                    print(pq[0][2])   # 输出堆顶任务的 tid

if __name__ == "__main__":
    main()