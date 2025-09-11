import bisect

def count_pairs(A, C):
    A.sort()
    
    sum_pairs = 0
    
    for a in A:
        target = a + count_pairs
        count = bisect.bisect_right(A, target) - bisect.bisect_left(A, target)
        
        sum_pairs += count
        
def main():
    n = int(input())
    A = list(map(int, input().split()))
    C = int(input())
    
    result = count_pairs(A, C)
    print(result)
    
if __name__ == "__main__":
    main()