"""
有一颗装满彩灯的二叉树, 树的每个节点代表一个灯泡。每个灯泡有三种颜色状态:
红色(用整数1表示)、绿色(用整数2表示)和蓝色(用整数3表示)。
每个节点上都配有一个开关, 当按下某个节点的开关时, 以该节点为根节点的子树上所有节点的灯泡颜色都会根据当前的颜色按照“红 -> 绿 -> 蓝 -> 红 -> …”的循环切换顺序切换一次颜色。

给定二叉树的初始颜色状态initial和目标颜色状态target, 两者都以层序遍历的一维整数数组的形式表示, 数组元素对应二叉树层序遍历的节点的颜色。
如果某个节点在二叉树中不存在, 则在数组中使用0表示。

目标是计算将二叉树从初始颜色状态initial切换到目标颜色状态target所需的最少开关切换次数。
"""
"""
输入：
7
1 2 3 1 2 3 1
3 1 2 3 1 2 1
"""
"""
输出：
3
"""

import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))    
    
    ans = 0
    
    def dfs(i, f):
        """i: 数组下标；f: 祖先累计偏移(0..2)"""
        nonlocal ans
        if i >= n or a[i] == 0:
            return
        
        cur = ((a[i] - 1) + f) % 3          # 当前实际颜色(0..2)
        tgt = (b[i] - 1) % 3                # 目标颜色(0..2) —— 题目保证存在节点时 b[i]∈{1,2,3}
        need = (tgt - cur) % 3              # 需在本节点再按的次数(0/1/2)
        ans += need
        nf = (f + need) % 3                 # 传给子树的新偏移
        dfs(2*i + 1, nf)
        dfs(2*i + 2, nf)
    
    dfs(0, 0)
    print(ans)

if __name__ == "__main":
    solve()