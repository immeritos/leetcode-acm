"""
Given a positive integer nn, you need to count the number of integers from 1 to n that satisfy the following condition: 
For each integer i, the sum of the digits of i modulo 10 equals the last digit of i.

Specifically, let S(i) be the sum of the digits of integer i, and d(i) be the last digit of integer i (i.e., i mod 10). 
We need to satisfy the following condition:
S(i) mod 10 = d(i)
S(i) mod 10 = d(i)

Please calculate the number of integers that satisfy the above condition.
"""

n = int(input())

count = 0

for i in range(n-1):
    digits = [(i+1)//10, (i+1)%10]
    total = sum(digits)
    if total%10 == digits[1]:
        count += 1
    else:
        continue
    
print(count)

"""
n = int(input())
count = 0

for i in range(1, n+1):
    dig_sum = sum([int(x) for x in str(i)])
    if i % 10 == dig_sum % 10:
        count += 1
        
print(count)
"""