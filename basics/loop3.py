"""
Given an integer array arr, find the maximum value in the array and its corresponding subscript sequence.

You need to write a program that outputs the maximum value in the array and all indexes where the maximum value occurs.
"""

n = int(input())
arr = list(map(int, intput().split))

max_value = max(arr)
indices = [str(index) for index, value in enumerate(arr) if value == max_value]

print(max_value)
print(' '.join(indices))