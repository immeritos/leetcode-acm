"""
Find the longest contiguous subarray of the same part in two difference arrays.
"""

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

diff_a = []
for i in range(n - 1):
    diff_a.append(arr[i + 1] - arr[i])

diff_b = []
for i in range(n - 1):
    diff_b.append(brr[i+1] - brr[i])
    
left = 0
right = 0
ans = 0
m = len(diff_a)

while left < m:
    while right < m and diff_a[right] == diff_b[right]:
        right += 1
    ans = max(ans, right-left)
    left = right + 1
    right = left
    
print(ans + 1)