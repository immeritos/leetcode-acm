"""
Use a recursive algorithm to implement a function that reverses a given string s.
You need to write a recursive function that accepts a string and returns the reversed version of the string. 
Note that the recursive condition is that the original string is returned only if the length of the string is 1 or empty.
"""

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

if __name__ == "__main__":
    s = input()
    print(reverse_string(s))