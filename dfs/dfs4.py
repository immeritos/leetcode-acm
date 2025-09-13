"""
Given an array nums containing n distinct integers, use the depth-first search (DFS) algorithm to find all possible permutations of the array.

Each element in the permutation must be unique and arranged in lexicographical order.
"""

import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def dfs(nums, path, visited, result):
    if len(path) == len(nums):
        result.append(path[:])
        return
    
    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            path.append(nums[i])
            dfs(nums, path, visited, result)
            path.pop()
            visited[i] = False

def main():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    nums.sort()
    
    result = []
    path = []
    visited = [False] * n
    dfs(nums, path, visited, result)
    
    for perm in result:
        print(" ".join(map(str, perm)))
        
if __name__ == "__main__":
    main()