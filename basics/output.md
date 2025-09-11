# 1️⃣ 数值格式化
## 1.1 基本小数格式
```python
pi = 3.141592653589793
print(f"原始值: {pi}")         # 原样输出
print(f"保留两位小数: {pi:.2f}")  # 四舍五入保留两位
```
## 1.2 按需保留小数位（自动去掉多余 0）
```python
# 规则：
# - 如果是整数，不显示小数点
# - 如果是小数，最多保留 3 位（四舍五入）
# - 末尾 0 自动去掉
values = [1.0, 1.10, 1.1116]
for val in values:
    print(f"{round(val, 3):g}")

# 输出：
# 1
# 1.1
# 1.112
```

## 1.3 科学计数法
```python
print(f"科学计数法: {pi:.2e}")  # 3.14e+00
```

3## 1.4 宽度与对齐
```python
num = 123.456
print(f"右对齐宽度10: {num:10.2f}")  # '    123.46'
print(f"左对齐宽度10: {num:<10.2f}")  # '123.46    '
print(f"居中对齐宽度10: {num:^10.2f}") # ' 123.46  '
```

## 1.5 千位分隔符
```python
n = 1234567890
print(f"千位分隔符: {n:,}")       # 1,234,567,890
print(f"千位分隔+两位小数: {n:,.2f}")  # 1,234,567,890.00
```
## 1.6 百分比
```python
rate = 0.1234
print(f"百分比: {rate:.2%}")  # 12.34%
```
## 1.7 不同进制
```python
x = 42
print(f"二进制: {x:b}")   # 101010
print(f"八进制: {x:o}")   # 52
print(f"十六进制: {x:x}") # 2a
```

# 2️⃣ 字符串格式化
```python
name = "Alice"
age = 25
print(f"姓名: {name}, 年龄: {age}")
print(f"大写姓名: {name.upper()}")
a, b = 3, 5
print(f"{a} + {b} = {a + b}")
print(f"{a=}, {b=}, {a+b=}")  # 调试输出（Python 3.8+）
```
# 3️⃣ 日期时间格式化
```python
from datetime import datetime
now = datetime.now()
print(f"当前时间: {now:%Y-%m-%d %H:%M:%S}")
```
# 4️⃣ 输出控制
```python
print("Hello", end="")               # 无换行输出
print("World")                        # 输出 HelloWorld
print("A", "B", "C", sep=", ")        # 自定义分隔符
arr = [1, 2, 3]
print(*arr)                           # 1 2 3
print(*arr, sep=",")                  # 1,2,3
```

```python
```

```python
```