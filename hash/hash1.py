"""
Tazi has a bag containing n integers. 
Now, he has Q questions, each asking how many times a specific number appears in the bag. 
Please help Tazi answer these questions.
"""

from collections import Counter

def main():
    n, Q = map(int, input().split())
    
    numbers = list(map(int, input().split()))
    
    count_map = Counter(numbers)
    
    for _ in range(Q):
        num = int(input())
        
        print(count_map.get(num, 0))
        
if __name__ == "__main__":
    main()