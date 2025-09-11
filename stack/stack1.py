"""
Given a string containing only two characters: '(' and ')', determine whether this string is a legal parenthesis sequence. 
A legal parenthesis sequence must satisfy the following conditions:

Every left parenthesis must have a corresponding right parenthesis.

Every right parenthesis must appear after its corresponding left parenthesis.
Parentheses must be paired, and nested parentheses must be valid.

For example, the strings "()" and "(())" are legal parenthesis sequences, while "(()" and "(((" are not.
"""

s = input().strip()
stack = []

for char in s:
    if char == '(':
        stack.append(char)
        
    elif char == ')':
        if not stack:
            print("No")
            exit(0)
        stack.pop()

if not stack:
    print("Yes")
else:
    print("No")