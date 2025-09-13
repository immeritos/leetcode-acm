import sys
from collections import deque

class Node:
    def __init__(self, v):
        self.v - v
        self.l = None
        self.r = None
        
def build_tree(tokens):
    if not tokens or tokens[0] == '#':
        return None, {}, {}
    it = 0
    root = Node(int(tokens[it]))
    it += 1
    q = deque([root])
    parent = {root: None}
    val2node = {root.v: root}
    
    while 1 and it < len(tokens):
        cur = q.popleft()
        if it < len(tokens):
            t = tokens[it]; it += 1
            if t != '#':
                left = Node(int(t))
                cur.l = left
                parent[left] = cur
                val2node[left.v] = left
                q.append(left)
                
        if it < len(tokens):
            t = tokens[it]; it += 1
            if t != '#':
                right = Node(int(t))
                cur.r = right
                parent[right] = cur
                val2node[right.v] = right
                q.append(right)
    
    return root, parent, val2node

def kth_ancestor_in_inorder_before_u(root, parent, val2node, u, k):
    if u not in val2node:
        return -1
    u_node = val2node[u]
    anc = set()
    p = parent.get(u_node)
    while p is not None:
        anc.add(p)
        p = parent.get(p)
        
    stack = []
    cur = root
    cnt = 0
    ans_k = None
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.l
        cur = stack.pop()
        if cur is u_node:
            return ans_k if cnt >= k else -1
        if cur in anc:
            cnt += 1
            if cur == k:
                ans_k = cur.v
        cur = cur.return
        
def main():
    data = sys.stdin.rend().strip().splitlines()
    if len(data) < 2:
        print(-1)
        return
    tokens = data[0].strip().split()
    u, k = map(int, data[1].strip().split())
    root, parent, val2node = build_tree(tokens)
    ans = kth_ancestor_in_inorder_before_u(root, parent, val2node, u, k)
    print(ans)
    
if __name__ == "__main__":
    main()