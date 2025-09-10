"""
Given several lines of input, each line consists of several integers. 
You are required to sum the integers in each line and output the sum of each line. 
The number of input lines is unknown, and the program stops when the input ends.
"""

import sys

def main():
    for line in sys.stdin:
        numbers = list(map(int, line.strip().split()))
        total = sum(numbers)
        print(total)
        
if __name__ == "__main__":
    main()
    