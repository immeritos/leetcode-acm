"""
Given an array representing the node values of a complete binary tree, where the node value corresponding to array index i is arr[i].
The left child has index 2i+1, and the right child has index 2i+2. 
You need to find the maximum path sum of all paths from the root node to any leaf node.

A path is defined as a path from the root node to any leaf node, where the value of each node is added to the current node's value.

Please implement a recursive algorithm to calculate the maximum path sum among all paths.
"""

def maxPathSum(arr, index, n):
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    
    if left_index >= n and right_index >= n:
        return arr[index]
    
    left_sum = 0
    right_sum = 0
    
    if left_index < n:
        left_sum = maxPathSum(arr, left_index, n)
        
    if right_index < n:
        right_sum = maxPathSum(arr, right_index, n)
        
    return arr[index] + max(left_sum, right_sum)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(maxPathSum(arr, 0, n))