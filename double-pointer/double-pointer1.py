"""
Given a sorted array nums and a target value, find two numbers in the array whose sum equals the target value and return their indices. 
Guarante that there is only one solution.

If no two numbers match the condition, return -1.
"""

def find_two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        sum_val = nums[left] + nums[right]
        if sum_val == target:
            return left + 1, right + 1
        elif sum_val < target:
            left += 1
        elif sum_val > target:
            right -= 1
            
    return -1

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

result = find_two_sum(nums, target)

if result == -1:
    print(-1)
else:
    print(result[0], result[1])