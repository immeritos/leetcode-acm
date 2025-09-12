"""
Given a string s, find the shortest substring containing all lowercase letters (a through z). If no such substring exists, return -1.

Note that the letters in the string do not need to be in order and may contain duplicates.
"""

def shortest_all_letters_substring(s):
    count = [0] * 26
    unique = 0
    n = len(s)
    min_len = n + 1
    left = 0
    
    for right in range(n):
        c = s[right]
        if 'a' <= c <= 'z':
            idx = ord(c) - ord('a')
            if count[idx] == 0:
                unique += 1
            count[idx] += 1
            
        while unique == 26:
            min_len = min(min_len, right - left + 1)
            cl = s[left]
            if 'a' <= cl <= 'z':
                idx = ord(cl) - ord('a')
                count[idx] -= 1
                if count[idx] == 0:
                    unique -= 1
            left += 1
            
    return min_len if min_len <= n else -1

if __name__ == "__main__":
    s = input().strip()
    print(shortest_all_letters_substring(s))