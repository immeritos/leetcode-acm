# 字符串切片的基本语法
```python
string[start:end:step]
```
- start：切片的起始位置，包含该位置。默认为 0，即从字符串的第一个字符开始。
- end：切片的结束位置，不包含该位置。默认为字符串的末尾，即提取到最后一个字符为止。
- step：步长，表示每次从起始位置到结束位置的跳跃量。默认为 1，即逐个字符获取。

## 1. 获取从某个位置到另一个位置的子字符串
```python
s = "abcdef"
print(s[1:4])  # bcd
```

## 2. 省略 start 和 end
```python
s[:]  # 'abcdef'
```

## 3. 使用步长 step
```python
s[::2]  # ace
```

## 4. 省略步长，使用负数步长（反转字符串）
```python
s[::-1]    # fedcba
s[5:2:-1]  # fed（从索引 5 到索引 3，逆向取）
```

## 5. 从指定位置开始，指定步长
```python
s[1::2]  # bdf
```

## 6. 负索引
```python
s[-3:]   # def（从倒数第三个开始到结尾）
s[:-2]   # abcd（去掉最后两个字符）
```

## 7. 超出索引范围
- 切片不会报错，超出范围会自动截断。
```python
s[2:100]    # cdef
s[-100:3]   # abc
```

## 8. 步长为负的情况
- 当 step < 0 时，start 必须大于 end 才能有结果，否则返回空字符串。
```python
s[5:2:-1]  # fed
s[2:5:-1]  # ''（空）
```

## 9. 判断回文字符串
```python
if string == string[::-1]:
    print("YES")
```

## 10. 将字符串 B 插入到字符串 A
```python
for i in range(len(A) + 1):
    new_string = A[:i] + B + A[i:]
```

## 11. 删除指定位置的字符
```python
s = "abcdef"
i = 2
new_s = s[:i] + s[i+1:]
print(new_s)  # abdef
```

## 12. 每个单词反转但保持顺序
```python
sentence = "hello world"
print(" ".join(word[::-1] for word in sentence.split()))
# olleh dlrow
```

## 13. 取奇数位 / 偶数位字符
```python
s = "abcdef"
print(s[::2])  # ace（偶数索引）
print(s[1::2]) # bdf（奇数索引）
```

## 14. 多层切片组合
```python
s = "abcdefghij"
print(s[::-1][::2])  # 逆序后再每隔一个取 → jhfdb
```

## 15. 用切片实现 rotate（循环位移）
```python
s = "abcdef"
k = 2
print(s[k:] + s[:k])   # 左移 2 位 → cdefab
print(s[-k:] + s[:-k]) # 右移 2 位 → efabcd
```