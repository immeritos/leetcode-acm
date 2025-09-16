"""
我们有 N 台服务器的物料编码，每个编码中分别包含一段代表 CPU 型号的子串(格式为C后跟两位数字)、一段代表内存型号的子串(M+两位数字)、一段代表主板型号的子串(B+两位数字)。
每个编码中，这三类备件可能出现多次，但我们只取各自第一次出现的型号；
然后统计所有服务器下线后，可回收的不同型号及对应数量，按型号字典序输出。
"""
"""
输入：
2
C01M23B050130 C01M23B060130
"""
"""
输出：
C01,2
M23,2
B05,1;B06,1
"""

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