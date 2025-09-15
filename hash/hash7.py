import re
import sys

def main():
    n = int(input())
    codes = input().split()
    
    cntCpu = {}
    cntMem = {}
    cntBoa = {}
    
    pCpu = re.compile(r'C\d{2}')
    pMem = re.compile(r'M\d{2}')
    pBoa = re.compile(r'B\d{2}')  
    
    for s in codes:
        m = pCpu.search(s)
        cpu = m.group() if m else ''
        m = pMem.search(s)
        mem = m.group() if m else ''
        m = pBoa.search(s)
        boa = m.group() if m else ''
        
        cntCpu[cpu] = cntCpu.get(cpu, 0) + 1  
        cntMem[mem] = cntMem.get(mem, 0) + 1   
        cntBoa[boa] = cntBoa.get(boa, 0) + 1  
        
    def fmt(d):
        items = sorted(d.items())
        return ';'.join(f"{k}, {v}" for k, v in items)
    
    print(fmt(cntCpu))
    print(fmt(cntMem))
    print(fmt(cntBoa))
    
if __name__ == "__main__":
    main()