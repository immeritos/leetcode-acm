"""
给定一棵 二叉树，树上每个节点代表一户居民。
需要在若干节点上建设基站，每个基站可以覆盖其所在节点及与其相邻的左右子节点和父节点，覆盖距离为 1。
求覆盖整棵树的最少基站数量。
"""
"""
输入：
1 2 3 4 N 5 6
"""
"""
输出：
2
"""

import sys
from collections import deque
sys.setrecursionlimit(1_000_000)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(vals):
    # 层序 + 'N' 表示空
    if not vals or vals[0] == 'N':
        return None
    root = TreeNode(int(vals[0]))
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        # 左孩子
        if i < len(vals) and vals[i] != 'N':
            node.left = TreeNode(int(vals[i]))
            q.append(node.left)
        i += 1
        # 右孩子
        if i < len(vals) and vals[i] != 'N':
            node.right = TreeNode(int(vals[i]))
            q.append(node.right)
        i += 1
    return root

def dfs(u):
    if not u:
        # (在本节点放基站, 本节点被覆盖无基站, 本节点未覆盖)
        return (float('inf'), 0, 0)
    L0, L1, L2 = dfs(u.left)
    R0, R1, R2 = dfs(u.right)
    # u 放基站
    f0 = 1 + min(L0, L1, L2) + min(R0, R1, R2)
    # u 被覆盖但不放基站（由某个孩子的基站覆盖）
    f1 = min(
        L0 + min(R0, R1),
        R0 + min(L0, L1)
    )
    # u 未覆盖（交给父节点来覆盖）
    f2 = L1 + R1
    return f0, f1, f2

def main():
    vals = sys.stdin.readline().split()
    root = build_tree(vals)
    f0, f1, _ = dfs(root)
    print(min(f0, f1))

if __name__ == "__main__":
    main()
