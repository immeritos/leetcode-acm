"""
Problem Description

Given a two-dimensional grid of size n * n.
You start at the top left corner (0,0) and can choose to go down or right. 
Each time you take a step, you can choose to move one square down or one square right. 
Count the number of unique paths from (0,0) to (n - 1,n - 1).
"""
"""
Input:

The input consists of an integer nn (1 <= n <= 15), representing the size of the grid.
"""
"""
Output:

Output an integer representing the number of unique paths from (0,0) to (n - 1,n - 1).
"""
def uniquePaths(x, y, n):
    if x == n - 1 and y == n - 1:
        return 1
    
    paths = 0
    
    if x < n - 1:
        paths += uniquePaths(x + 1, y, n)
        
    if y < n - 1:
        paths += uniquePaths(x, y + 1, n)
        
    return paths

if __name__ == "__main__":
    n = int(input())
    print(uniquePaths(0, 0, n))