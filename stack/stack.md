# 1. 栈的定义

栈（Stack）是一种常见的线性数据结构，其特点是遵循“后进先出”（LIFO，Last In First Out）原则。也就是说，最后被压入栈中的元素会最先被弹出。

# 2. 栈的基本操作包括：

- 入栈（Push）：将一个元素添加到栈的顶部。
- 出栈（Pop）：移除栈顶元素，并返回该元素。
- 查看栈顶元素（Peek 或 Top）：返回栈顶的元素，但不移除它。
- 判断栈是否为空（IsEmpty）：检查栈是否没有任何元素。

# 3. 栈的特性：

- LIFO原则：栈中的元素是从栈顶添加和移除的，栈顶的元素是最先被访问的。
- 只能在一端操作：栈的操作只能在栈顶进行。

# 4. 栈的应用：

- 函数调用管理：在程序运行过程中，函数调用的顺序和返回都由栈来管理。每次函数调用时，程序会把当前函数的信息压入栈中，函数执行完成后会从栈中弹出，返回到调用函数的位置。
- 表达式求值：栈常用于数学表达式的求值，尤其是处理括号匹配和运算符优先级时。
- 浏览器的历史记录：浏览器在你浏览网页时会将每个页面的链接压入栈中，这样你按回退按钮时就可以弹出最近访问的页面。

# 5. 栈的实现：

栈可以通过数组或链表来实现。常见的实现方式有：

- 数组实现：使用数组来存储栈的元素，栈顶指针记录栈顶元素的位置。
- 链表实现：通过链表的头结点来表示栈顶，头结点指向栈顶元素。

栈的操作时间复杂度通常是 O(1)，即每次操作的时间是常数级别的，因为它只涉及栈顶元素。


# 6. Python中的栈实现
Python没有专门的栈类型，我们通常使用列表 list 来模拟栈操作，利用 append() 来压栈，利用 pop() 来弹栈。 
```python
# 使用 list 模拟栈
stack = []

# 入栈
stack.append(1)
stack.append(2)
stack.append(3)
print("入栈后:", stack)  # [1, 2, 3]

# 出栈
top = stack.pop()
print("出栈元素:", top)   # 3
print("当前栈:", stack)   # [1, 2]

# 查看栈顶元素
print("栈顶元素:", stack[-1])  # 2

# 判断是否为空
print("栈是否为空:", len(stack) == 0)  # False

```

# 7. Python中的pop实现
在 Python 中，pop() 和 pop(i) 都是列表（list）对象的常用方法，用于移除并返回指定位置的元素。它们的区别在于删除的元素的具体位置。下面是它们的简要讲解和区别：
## 7.1. pop()
- pop() 默认删除并返回列表中的 最后一个 元素。
```python
list.pop()
```

```python
lst = [1, 2, 3, 4, 5]
last_element = lst.pop()  # 删除并返回最后一个元素
print(last_element)  # 输出: 5
print(lst)           # 输出: [1, 2, 3, 4]
```

## 7.2. pop(i)
pop(i) 允许你删除并返回 指定索引位置 i 的元素。如果你指定的索引 i 超出了范围，会引发 IndexError 错误。
```python
list.pop(i)
```

```python
lst = [1, 2, 3, 4, 5]
element = lst.pop(2)  # 删除并返回索引为2的元素
print(element)  # 输出: 3
print(lst)      # 输出: [1, 2, 4, 5]
```

```python
lst = [1, 2, 3, 4, 5]
element = lst.pop(-2)  # 删除并返回倒数第二个元素
print(element)  # 输出: 4
print(lst)      # 输出: [1, 2, 3, 5]
```

## 7.3. 总结
pop()：
- 删除并返回列表的 最后一个 元素。
- 适用于快速删除末尾元素，时间复杂度是 O(1)。

pop(i)：
- 删除并返回指定索引位置 i 的元素。
- 适用于删除列表中的任意元素，时间复杂度是 O(n)，因为删除元素后需要移动剩余的元素。

## 7.4. 使用场景
pop()：通常用于处理栈（后进先出，LIFO）结构，删除并获取最后添加的元素。
pop(i)：用于删除列表中间或者指定位置的元素，在一些需要动态修改列表内容的场景中使用，比如删除某个特定的元素。

# 8. 自定义栈类（面试常考）
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("栈为空，无法出栈")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


# 测试
s = Stack()
s.push(5)
s.push(10)
print("栈顶:", s.peek())   # 10
print("出栈:", s.pop())    # 10
print("栈是否为空:", s.is_empty())  # False
```
