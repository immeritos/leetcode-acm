"""
Given two strings A and B, determine whether string B can be inserted at a certain position in string A,
so that the new string becomes a palindrome. 
A palindrome is a string that is the same when read forward and backward.
Note: It can be inserted at the beginning or end.
"""

def main():
    A = input().strip()
    B = input().strip()
    
    for i in range(len(A)+1):
        new_string = A[:i] + B + A[i:]
        
        if new_string == new_string[::-1]:
            print("YES")
            return
        
    print("NO")
    
if __name__ == "__main__":
    main()