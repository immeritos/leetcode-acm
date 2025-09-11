# 哈希表（Hash Table）

哈希表是一种基于哈希函数（Hash Function）的数据结构，用于实现键值对的快速存储和查找。它的主要特点是：

1. 快速查找：平均情况下，哈希表的查找、插入和删除操作的时间复杂度都是 O(1)。

2. 键值对存储：哈希表存储的是键值对，每个键（Key）唯一对应一个值（Value）。

3. 哈希函数：通过哈希函数将键映射到哈希表中的位置，从而实现快速存取。


# Python 中的 dict
在 Python 中，dict 是内置的哈希表实现，它可以用于存储键值对，并提供快速的查找、插入和删除操作。dict 的内部实现使得查找和插入操作的平均时间复杂度为 O(1)，因此它非常适合用于实现哈希表的功能。
Python 中的 dict

dict 是 Python 的一个核心数据结构，允许你通过键（key）来访问对应的值（value）。它的基本操作包括插入、查询、更新和删除，所有这些操作的平均时间复杂度通常是 O(1)。
## 创建和使用 dict
1. 创建一个 dict： 你可以通过 {} 或 dict() 来创建一个空的字典，或者通过键值对初始化。
```python
my_dict = dict()  # 创建一个空字典
my_dict = {"apple": 1, "banana": 2}  # 创建一个带有初始键值对的字典
```
2. 插入元素： 通过键来访问字典，并赋值给该键。
```python
my_dict["orange"] = 3  # 插入一个新的键值对
print(my_dict)  # 输出：{'apple': 1, 'banana': 2, 'orange': 3}
```
3. 查询元素： 使用键来获取对应的值。如果键不存在，可以使用 get() 方法，它会返回一个默认值（如 None 或自定义值）。
```python
print(my_dict["apple"])  # 输出：1
print(my_dict.get("grape", 0))  # 输出：0，因为 "grape" 不在字典中
```
4. 更新元素： 直接通过键来修改值。
```python
my_dict["apple"] = 4  # 更新值
print(my_dict)  # 输出：{'apple': 4, 'banana': 2, 'orange': 3}
```
5. 删除元素： 使用 del 或 pop() 来删除键值对。
```python
del my_dict["banana"]  # 删除键 "banana"
print(my_dict)  # 输出：{'apple': 4, 'orange': 3}
```
```python
value = my_dict.pop("orange", None)  # 删除并返回 "orange" 对应的值
print(my_dict)  # 输出：{'apple': 4}
print(value)  # 输出：3
```
6. 字典视图对象
```python
d = {"a": 1, "b": 2}
print(d.keys())   # dict_keys(['a', 'b'])
print(d.values()) # dict_values([1, 2])
print(d.items())  # dict_items([('a', 1), ('b', 2)])
```
7. 合并字典
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(d1 | d2)  # Python 3.9+ 新语法 → {'a': 1, 'b': 3, 'c': 4}
```


# 时间复杂度分析

时间复杂度衡量的是算法执行所需的时间增长率，随着输入规模的增加，算法的运行时间如何变化。常见的时间复杂度包括：

- `O(1)`：常数时间，无论输入规模多大，执行时间保持不变。

- `O(log n)`：对数时间，随着输入规模增加，执行时间按对数增长。例如二分操作。

- `O(n)`：线性时间，执行时间与输入规模成正比。

- `O(n log n)`：线性对数时间，常见于高效排序算法如快速排序、归并排序。

- `O(n²)`：平方时间，常见于简单的嵌套循环，如冒泡排序。

## dict的时间复杂度
- 查询和插入：对于字典的查询和插入操作，平均时间复杂度是 `O(1)`，即无论字典的大小如何，执行这些操作所需的时间几乎是恒定的。

- 删除：删除操作的时间复杂度也是 `O(1)`，但在最坏情况下（例如哈希冲突非常严重时），它可能退化为 `O(n)`，但这种情况非常少见。




# Python 中的collections.Counter

在 Python 中，Counter 是 collections 模块中的一个哈希表实现，属于 dict 字典的子类，用于统计元素的频率。它非常适合解决这类统计问题。
1. 键值对存储：Counter 存储的是数字及其出现次数的键值对。
```python
# 创建一个 Counter 来统计数字的频率
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(numbers)
```
2. 快速访问：查询某个数字的出现次数是常数时间复杂度 O(1)。
```python
# 快速查找某个数字的出现次数
print(counter[2])  # 输出 2，因为数字 2 出现了 2 次
print(counter[3])  # 输出 3，因为数字 3 出现了 3 次
```
## 主要操作的示例代码

在 Counter 中，除了常规的插入和访问操作外，还提供了许多便利的功能：
1. 插入或更新元素的频率：
```python
from collections import Counter

counter = Counter()

# 插入元素
counter["apple"] += 1
counter["banana"] += 2

# 更新元素
counter["apple"] += 3

print(counter)  # 输出：Counter({'apple': 4, 'banana': 2})
```
2. 获取最常见的元素：
Counter 还提供了 most_common 方法，返回出现频率最高的元素及其频次。
```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(numbers)

# 获取出现频率最高的前两个元素
print(counter.most_common(2))  # 输出：[(4, 4), (3, 3)]
```
3. 删除元素：
如果需要删除某个键值对，可以使用 del 或 subtract 方法。
```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(numbers)

# 删除数字 2
del counter[2]

# 减去某个元素的频率
counter.subtract([3])

print(counter)  # 输出：Counter({4: 4, 3: 2, 1: 1})
```
4. 统计多个元素：
Counter 也支持对多个 Counter 进行合并，使用 + 或 update() 方法。
```python
from collections import Counter

counter1 = Counter([1, 2, 3])
counter2 = Counter([3, 4, 5])

# 合并两个 Counter
combined_counter = counter1 + counter2
print(combined_counter)  # 输出：Counter({3: 2, 1: 1, 2: 1, 4: 1, 5: 1})
```


# Python 中的collections.defaultdict
collections.defaultdict 是 dict 的子类，它能在访问不存在的键时，自动初始化默认值，而不是抛出 KeyError
```python
from collections import defaultdict

# 创建一个默认值为 list 的 defaultdict
d = defaultdict(list)

d["a"].append(1)   # 不需要先判断键是否存在
d["a"].append(2)
d["b"].append(3)

print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})
```
## 常见场景

1. 分组
```python
words = ["apple", "banana", "avocado", "blueberry"]
grouped = defaultdict(list)
for w in words:
    grouped[w[0]].append(w)
print(grouped)  # {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}
```
2. 构造多重映射
```python
graph = defaultdict(set)
graph["A"].add("B")
graph["A"].add("C")
print(graph)  # {'A': {'B', 'C'}}
```
