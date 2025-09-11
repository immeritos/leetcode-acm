定义一个空列表
```python
a = []
```

定义一个包含元素的列表
```python
b = [1, 2, 3, 4, 5]
```

使用列表推导式创建列表
```python
c = [i for i in range(10)]

print(a)  # 输出: []
print(b)  # 输出: [1, 2, 3, 4, 5]
print(c)  # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
动态扩展：列表的大小可以动态改变，可以随时添加或删除元素
```python
b.append(6)    # 在列表末尾添加元素6
b.insert(0, 0) # 在索引0的位置插入元素0
print(b)       # 输出: [0, 1, 2, 3, 4, 5, 6]

b.pop()        # 删除并返回最后一个元素
print(b)       # 输出: [0, 1, 2, 3, 4, 5]

del b[0]       # 删除索引0的元素
print(b)       # 输出: [1, 2, 3, 4, 5]
```

range() 函数生成一个整数序列，常用于需要循环固定次数的情况：
```python
for i in range(5):
    print(f"当前i的值: {i}")
```

指定起始和结束：
```python
for i in range(1, 6):
    print(i)
```

指定步长：
```python
for i in range(0, 10, 2):
    print(i)
```

反向遍历：
```python
for i in range(5, 0, -1):
    print(i)
```

列表推导式，基于已有的可迭代对象快速生成新的列表：
```python
# 列表推导式生成 1 到 5 的平方数
squares = [x ** 2 for x in range(1, 6)]  # 输出 [1, 4, 9, 16, 25]
```
```python
```
```python
```