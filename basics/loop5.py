"""
Given an integer matrix matrix, you need to process multiple queries. 
Each query contains the coordinates of the upper left corner and lower right corner of a submatrix [(x1,y1),(x2,y2)], 
and you need to find the maximum value in the submatrix.
"""

def main():
    n, m = map(int, input().split())
    
    matrix = []
    for i in range(n):
        row = list(map(int, intput().split()))
        matrix.append(row)
        
    q = int(intput())
    
    while q > 0:
        q -= 1
        x1, y1, x2, y2 = map(int, input().split())
        
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        max_val = matrix[x1][y1]
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                max_val = max(max_val, matrix[i][j])
                
        print(max_val)
        
if __name__ == "__main__":
    main()