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