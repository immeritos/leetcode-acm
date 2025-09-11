输入整数
```python
n = int(input())
```
输入多个整数
```python
n, m = map(int, input().split())
```

输入数组元素列表
```python
arr = list(map(int, intput().split()))
```

读取带逗号的元素列表
```python
arr = list(map(int, input().split(',')))  
# split(',') 不能自动去掉空格，可配合 strip()
```

输入多行数组元素列表
```python
import sys
for line in sys.stdin:
    arr = list(map(int, line.strip().split()))
    # 这里建议加 strip()
    # 原因：sys.stdin 读取的行结尾一定有 '\n'，而且 split() 不会自动去掉指定分隔符以外的字符
    # 如果改成 split() 而不 strip()，一般也没问题，但有时会留尾部符号
```

读取固定行数
```python
n = int(input())
lines = [input().strip() for _ in range(n)]  
```

构造矩阵
```python
matrix = [[0 for _ in range(m)] for _ in range(n)] #外层行，内层列

for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input())
        # 这种单个数字输入，不需要 strip()
```
如果矩阵是按行输入
```python
matrix = [list(map(int, input().split())) for _ in range(n)]  
# 直接 split() 即可
```

访问行
```python
matrix[i]      # 第 i 行（整行）
matrix[i][:]   # 第 i 行的所有列
```


访问列
```python
[row[j] for row in matrix] # 第 j 列
```

输入字符串 A 和 B, 如"abc""abcabcabc"
```python
A = input().strip()  # 必须 strip()，否则会带上换行符
B = input().strip()  # 字符串输入通常建议 strip()
```
读取全部内容
```python
import sys
data = sys.stdin.read().strip().split()  
# 读到 EOF，再按空白分割成列表
```

快速读取大量数字
```python
import sys
input = sys.stdin.readline  # 用更快的 readline 替代 input
```

将二维输入直接转成numpy数组
```python
import numpy as np
arr = np.loadtxt(sys.stdin, dtype=int)  
```