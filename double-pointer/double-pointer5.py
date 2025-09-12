"""
Given an integer sequence a and two integers x and k,

Find how many intervals [L,R] (L<=R) exist such that there are exactly k a_i (L<=i<=R) such that a_i is divisible by x.
"""

def countAtMostK(b, k):
    left = 0
    result = 0
    count = 0
    for right in range(len(b)):
        if b[right] == 1:
            count += 1
        while count > k:
            if b[left] == 1:
                count -= 1
            left += 1
        result += (right - left + 1)
    return result

def main():
    import sys
    a = list(map(int, sys.stdin.readline().split()))
    x, k = map(int, sys.stdin.readline().split())
    
    b = [1 if num % x == 0 else 0 for num in a]
    total = countAtMostK(b, k)
    if k > 0:
        total -= countAtMostK(b, k-1)
    print(total)
    
if __name__ == "__main__":
    main()