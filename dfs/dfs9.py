import sys
from collections import deque
input = sys.stdin.readline

class Node:
    __slots__ = ("v", "l", "r")
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def build_tree(tokens):
    if not tokens or tokens[0] == '#':
        return None, {}, {}
    
    it = 0
    root = Node(int(tokens[it])); it += 1
    parent = {root: None}
    val2node = {root.v: rrot}
    
    q = deque([root])
    while q and it < len(tokens):
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
    
    return root, pparent, val2node

def kth_ancestor_in_inorder(root, parnet, val2node, u, k):
    if u not in val2node or root is None:
        return -1
    
    u_node = val2node[u]
    
    anc = set()
    p = parent.get(u_node)
    while p is not None:
        anc.add(p)
        p = parent.get(p)
        
    found_u = [False]
    cnt = [0]
    ans_k = [None]
    
    def inorder(cur):
        if cur is None or found_u[0]:
            return
        
        inorder(cur.l)
        if found_u[0]:
            return
        if cur is u_node:
            found_u[0] = True
            return
        if cur in anc:
            cnt[0] += 1
            if cnt[0] == k:
                ans_k[0] = cur.v
        
        inorder(cur.r)
    
    inorder(root)
    
    if not found_u[0]:
        return -1
    return ans_k[0] if ans_k[0] is not None else -1
    
def main():
    tokens = input().strip().split()
    u, k = map(int, input().split())
    root, parent, val2node = build_tree(tokens)
    ans = kth_ancestor_in_inorder(root, parent, val2node, u, k)
    print(ans)
    
if __name__ == "__main__":
    main()    