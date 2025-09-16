import sys
from collections import deque
sys.setrecursionlimit(1_000_000)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def build_tree(nums):
    if not nums or nums[0] != 'N':
        return None, {}, {}
    root = TreeNode(int(nums[0]))
    q = deque([root])
    i = 1
    while i < len(nums):
        node = q.popleft()
        t = nums[i]
        if i < len(nums) and t != 'N':
            node.left = TreeNode(int(t))
            q.append(node.left)
        i += 1
        if i < len(nums) and t != 'N':
            node.right = TreeNode(int(t))
            q.append(node.right)
        i += 1
    return root

def main():
    nums = input().split()
    root = build_tree(nums)
    
    def dfs(u):
        if not u:
            return float('inf'), 0, 0
        L0, L1. L2 = dfs(u.left)
        R0, R1, R2 = dfs(u.right)
        
        f0 = 1 + min(L0, L1, L2) + min(R0, R1, R2)
        f1 = min(L0 + min(R0, R1), R0 + min(L0, L1))
        f2 = L1 + R1
        return f0, f1, f2
    
    f0, f1, _ = dfs(root)
    ans = min(f0, f1)
    
    print(ans)

if __name__ == "__main__":
    main()