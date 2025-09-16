"""
安全分析师小王正在开发一款先进的入侵检测系统(IDS), 旨在实时监控网络流量并识别潜在的恶意活动。
系统将网络抽象为一个下标从0开始的整数数组 node_scores, 其中每个元素代表对应位置的安全评分：
正值表示安全或有正面安全措施, 负值表示存在潜在风险或威胁。 
分析师从入口节点(下标0)开始, 每一步最多可以前进K步, 但不能超出数组边界。
也就是说, 如果当前位于下标i, 则可以跳到任意下标j, 满足

i+1<=j<=min(n-1,i+K)

目标是到达下标n-1(最后一个监控点), 并使累积的安全评分总和最大。
注意：路径上的评分可能为正也可能为负。
"""
"""
输入：
2
8
3 -5 -10 2 -1 5 -6 -5
"""
"""
输出：
0
"""
import sys
from collections import deque

def max_score(node_scores, k):
    n = len(node_scores)
    dp = [-10**18] * n
    dp[0] = node_scores[0]
    
    dq = deque([0])
    
    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()
        dp[i] = dp[dq[0]] + node_scores[i]
        while dq and dp[dq[-1]] <= dq[i]:
            dq.pop()
        dq.append(i)
    
    return dp[-1]

if __name__ == "__main__"":
    K = int(input())
    n = int(input())
    scores = list(map(int, input().split()))
    print(max_score(scores, K))