"""
Given two strings A and B, determine whether string B can be constructed by concatenating multiple copies of A. 
In other words, determine whether there exists a non-negative integer k such that B equals k copies of A, i.e.,
B = A + A + … + A(k times)
If B can be represented as multiple copies of A, output "Yes"; otherwise, output "No".
"""

def main():
    
    A = input().strip()
    B = input().strip()
    
    lenA = len(A)
    lenB = len(B)
    
    if lenB % lenA != 0:
        print("No")
        return
    
    k = lenB // lenA
    constructed = A * k
    
    if constructed == B:
        print("Yes")
    else:
        print("No")
        
if __name__ = "__main__":
    main()