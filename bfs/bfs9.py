import sys
from collections import deque
input = sys.stdin.readline

def main():
    cars = list(map(int, input().split()))
    req = list(map(int, input().split()))
    
    if not cars or not req:
        print(-1)
        return
    
    carQ = deque(cars)
    genQ = deque(req)
    
    while carQ and genQ:
        K = carQ[0]
        need = genQ[0]
        
        if K == need:
            carQ.popleft()
            genQ.popleft()
        elif K > need:
            total = 0
            count = 0
            for val in genQ:
                if total + val <= K:
                    total += val
                    count += 1
                else:
                    break
            
            for _ in range(count):
                genQ.popleft()
            carQ.popleft()
        else:
            genQ.rotate(-1)
    
    print(len(genQ))

if __name__ == "__main__":
    main()
    