"""
Given an integer array arr, you need to implement a matching game. The rules of the game are as follows:

If there are three consecutive identical integers in the array, they are removed.

After removal, the elements in the array are shifted left to fill the gaps, potentially creating new consecutive identical elements.

You need to repeat this process until there are no more three consecutive identical integers in the array.

Please implement a function that returns the final array result.
"""

def eliminate_game(arr):
    stack = []
    
    for num in arr:
        stack.append(num)
        
        if len(stack) >= 3 and stack[-1] == stack[-2] == stack[-3]:
            stack.pop()
            stack.pop()
            stack.pop()
            
    return stack

def main():
    arr = list(map(int, input().split()))
    
    result = eliminate_game(arr)
    
    if not result:
        print("[]")
    else:
        print(" ".join(map(str, result)))