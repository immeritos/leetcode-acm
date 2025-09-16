"""
公司运动协会正在举办打气球游戏。打气球游戏规则如下：

墙上有一串各种颜色的气球，我们要给他尽可能多的分组，让相同颜色的气球在同一组内。

而且划分完的气球片段按顺序连接起来仍然是原始气球串

请返回一个列表表示划分完的气球片段长度，请注意，如果划分的片段有多个，各个片段之间以逗号和空格分割。
"""
"""
输入：一个字符串 s ，代表一串不同颜色的气球。字符串仅仅由小写英文字母组成。
abcdeabl
"""
"""
输出：一个列表，代表划分完之后的每个气球片段的长度。
[7, 1]
"""

def partition_balloon(s):
    last = {c: i for i, c in enumerate(s)}
    res = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            res.append(i - start + 1)
            start = i + 1
    return res

if __name__ == "__main__":
    s = input().strip()
    res = partition_balloon(s)
    print(res)