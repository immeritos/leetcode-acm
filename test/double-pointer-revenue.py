"""
某市场举办小吃节, 小吃节持续n天, 每天都会有不同的小吃摊位入驻, 每个摊位每天在投入一定的人力之后产生一定的营业额。

管理方希望在小吃节期间选择连续的若干天, 使得这些天的总营业额最大。但是由于人力限制, 选择这些天中总的人力不超过K人天。

请你计算出满足条件的最大营业额。
"""
"""
输入：
6 6
3 1
1 2
5 1
2 3
7 2
4 4
"""
"""
输出：
14
"""

def max_revenue(n, K, revenues, manpowers):
    ans = 0
    sum_rev = 0
    sum_man = 0
    left = 0
    
    for right in range(n):
        sum_rev += revenues[right]
        sum_man += manpowers[right]
        
        while left <= right and sum_man > K:
            sum_rev -= revenues[left]
            sum_man -= manpowers[left]
            left += 1
            
        ans = max(ans, sum_rev)
    return ans

if __name__ == "__main__":
    n, K = map(int, input().split())
    revenues = []
    manpowers = []
    for _ in range(n):
        r, m = map(int, input().split())
        revenues.append(r)
        manpowers.append(m)
    print(max_revenue(n, K, revenues, manpowers))