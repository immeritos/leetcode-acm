"""
有一队粮食车队, 每队运来K辆粮车;

有若干副将按序排队, 每人需求若干辆粮车;

规则：
    当前车队粮车数为K。
    若K=当前副将需求, 则该副将和车队同时出列;
    若K>当前副将需求, 设前i名副将总需求 S_i=sumr_j.
    找最大i,使得 S_i<=K<S_i+1,则前i 名副将和车队同时出列。
    若K<当前副将需求, 则该副将移到队尾, 车队保留在队首, 继续本车队的领取尝试。

重复直到车队或副将任意一方耗尽, 输出最终剩余未领到粮食的副将人数。
"""
"""
输入：
3 5 7 3 4
2 4 8 5 2
"""
"""
1
"""

import sys
from collections import deque
input = sys.stdin.readline

def main():
    cars = list(map(int, input().split()))
    req = list(map(int, input().split()))
    
    if not cars or not req:
        print(-1)
        return
    
    if any(x<1 or x>100 for x in cars+req):
        print(-1)
        return

    genQ = deque(req)

    for K in cars:
        if not genQ:
            break

        # 先在至多一整圈内寻找“能被这支车队喂到”的队首
        found = False
        for _ in range(len(genQ)):
            if genQ[0] <= K:
                found = True
                break
            genQ.rotate(-1)  # 让不满足的人排到队尾

        if not found:
            # 没人能被这支车队喂到 → 空车离开
            continue

        # 批量喂：从队首开始尽量多喂（累加前缀）
        used = 0
        while genQ and used + genQ[0] <= K:
            used += genQ.popleft()

        # 这支车队完成，换下一支（自然进入下一次 cars 遍历）

    print(len(genQ))

if __name__ == "__main__":
    main()

    