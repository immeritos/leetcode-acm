"""
本题定义的连通网络, 是由有连接关系的一个或多个节点组成的无向图。
图中有n个节点, n 的取值范围为 [1,160]。
每个节点有一个唯一的权重, 权重的取值范围为 [1,10000]。
节点之间有m条连接关系, m的取值范围为 [0,160], 每条连接表示无向边。
一个连通网络的权重定义为其所有节点权重之和；因为节点权重互不相同, 连通网络内部可以确定“权重最大的节点”。
要求：找到权重最大的连通网络, 输出该网络中权重最大的节点的名称, 以及该网络的总权重。题目保证不同连通网络的总权重不会相同。

"""
"""
输入：
5
node1 15
node2 12
node3 13
node4 4
node5 50
3
node1 node2
node3 node2
node4 node5
"""
"""
输出：
node5 54
"""

import sys
sys.setrecursionlimit(1_000_000)

def main():
    n = int(input())
    id_map = {}
    names = []
    weight = []
    for _ in range(n):
        line = input().split()
        names.append(line[0])
        weight.append(int(line[1]))
        id_map[line[0]] = i
        
    m = int(input().strip())
    adj = [[] fot _ in range(n)]
    for _ in range(m):
        u, v = input().split()
        iu, iv = id_map[u], id_map[v]
        adj[iu].append[iv]
        adj[iv].append[iu]
        
    visited = [False] * n
    best_sum = 0
    best_node = ""
    
    def dfs(u):
        visited[u] = True
        total = weight[u]
        max_idx = u
        for v in adj[u]:
            if not visited[v]:
                s, mi = dfs(v)
                total += s
                if weight[mi] > weight[max_idx]:
                    max_idx = mi
        return total, max_idx
    
    for i in range(n):
        if not visited[i]:
            s, mi = dfs(i)
            if s > best_sum:
                best_sum = s
                best_node = names[mi]
                
    print(best_node, best_sum)
    
if __name__ == "__main__":
    main()