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
        K = carQ.popleft()
        attempts = len(genQ)
        fed = False
        
        for _ in range(attempts):
            need = genQ[0]
            if need <= K:
                total = 0
                while genQ and total + genQ[0] <= K:
                    total += genQ.popleft()
                fed = True
                break
            else:
                genQ.rotate(-1)
    
    print(len(genQ))
    
    