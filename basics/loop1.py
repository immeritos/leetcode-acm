"""
Two scales are filled with different objects. 
The left scale has n objects, and the right scale has mm objects. 
We want to know whether the weights of the objects on the two scales are equal. 
If they are equal, he will return "Equal"; otherwise, he will return "Not Equal."
"""

n, m = map(int, input().split())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

left_total = sum(left)
right_total = sum(right)

if left_total == right_total:
    print("Equal")
else:
    print("Not Equal")