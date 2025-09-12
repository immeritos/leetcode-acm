# 双指针算法概述

双指针算法（双指针技术）是一种在处理线性数据结构（如数组、链表）时常用的算法策略。它通过同时使用两个指针，以不同的方式遍历数据结构，从而优化时间复杂度或简化问题的解决过程。双指针算法广泛应用于各种经典问题，如数组排序、链表操作、字符串处理等。
双指针的常见类型

1. 快慢指针（快指针与慢指针）
- 链表类
 - 检测环（Floyd 判圈法）
 - 找链表中点（快走 2，慢走 1）
 - 删除倒数第 k 个节点

- 数组类
 - 判定是否存在循环（如环形数组遍历问题）

2. 左右指针（双端指针）
- 用途：常用于处理有序数组中的问题，如两数之和、三数之和、四数之和等。
- 原理：设定一个指针指向数组的起始位置，另一个指针指向数组的末尾，根据当前指针对应的值与目标值的关系来移动指针，以缩小搜索范围。

3. 滑动窗口
- 子数组 / 子串问题
 - 最长不含重复元素的子串
 - 最短覆盖子串
 - 和小于 / 大于某值的子数组
 - 至多 / 恰好 k 个某元素的子区间
- 原理：通过两个指针定义一个窗口的左右边界，根据窗口内元素是否满足条件来动态调整窗口的大小和位置。

4. 区间双指针（双序列问题）

- 判断一个数组是否是另一个的子序列
- 合并两个有序数组 / 找公共子区间
- 差分数组匹配、最长公共片段（如你给的“两个数组的最长相同差分子段”）

# 构造思路

1. 明确问题是左右夹逼还是窗口滑动

- 若涉及「排序数组」和「两端逼近目标」 -> 用左右指针。

- 若涉及「连续子串/子区间」 -> 用滑动窗口。

- 若涉及「链表结构/环检测」 -> 用快慢指针。

2. 左右指针问题

- 初始 left=0, right=n-1，根据目标条件移动一端指针。

- 每次移动指针时，搜索空间严格缩小。

3. 滑动窗口问题

- 初始 left=0，遍历 right。

- 用 while 循环缩小窗口，直到满足条件。

- 在窗口调整的过程中，更新答案（最大值/最小值/计数）。

4. 快慢指针问题

- 快指针走两步，慢指针走一步。

- 根据相遇 / 偏移关系，得出答案。

# Python 常见写法模板
1. 快慢指针（链表判环）
```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
2. 左右指针（Two Sum II）
```python
def two_sum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return l, r
        elif s < target:
            l += 1
        else:
            r -= 1
    return -1
```
3. 滑动窗口（最长不重复子串）
```python
def lengthOfLongestSubstring(s):
    seen = set()
    l = 0
    res = 0
    for r, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[l])
            l += 1
        seen.add(ch)
        res = max(res, r - l + 1)
    return res
```

4. 滑动窗口（最小覆盖子串）
```python
from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    l = start = end = 0
    for r, ch in enumerate(s, 1):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if end == 0 or r - l < end - start:
                start, end = l, r
            need[s[l]] += 1
            if need[s[l]] > 0:
                missing += 1
            l += 1
    return s[start:end]
```