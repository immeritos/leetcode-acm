"""
There's a person named Xiaohong who loves tea. 
She has x strange cups, each of which can hold a positive integer. 
Xiaohong decides to push the numbers in these cups onto a stack, but she has a few rules: 

Each time she pushes a number onto the stack, 
if the top number is the same as the previous number, 
she takes the two numbers out, adds them together, and pushes the sum back onto the stack. 

Furthermore, if the top number is equal to the sum of the y consecutive numbers below it (1 ≤ y ≤ x), 
she takes the y+1 numbers out, adds them together, and pushes the sum back onto the stack. 

Of course, if neither of these two rules is met, she won't do anything. 
Now, Xiaohong pushes a series of positive integers onto the stack one by one. Tell her what the final number on the stack will be.
"""

maxn = 1010
stack = [0] * maxn
top = 0

arr = list(map(int, input().split()))

for x in arr:
    while True:
        flag = False
        tmp = 0
        
        for i in range(top, -1, -1):
            tmp += stack[i]
            
            if tmp == x:
                x += tmp
                top = i - 1
                flag = True
                break
        
        if not flag:
            break
    
    top += 1
    stack[top] = x
    
while top>0:
    print(stack[top], end=" ")
    top -= 1