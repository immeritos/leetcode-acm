"""
KNN 算法的核心思想是, 如果一个样本在特征空间中的 K 个最相邻的样本中的大多数属于某一个类别, 则该样本也属于这个类别, 并具有这个类别上样本的特性。
请按照下面的步理, 实现 KNN 算法。
KNN 算法说明：
计算待分类点到其他样本点的距离；
通过距离进行排序, 选择距离最小的 K 个点；
提取这 K 个临近点的类别, 根据少数服从多数的原则, 将占比最多的那个标签赋值给待分类样本点的 label 。
本题说明：
1、给定数据集中, 默认每一类标签都存在数据, 不存在某类型数量为 0 的场景；
2、为消除不同特征权重问题, 给出数据均已做好归一化处理, 并保留两位小数；
3、出现并列第一的情形时, 取并列第一的样本中, 最近邻居的标签返回；
4、距离函数为欧氏距离
"""
"""
输入：
3 10 2 3
0.81 0.64
0.19 0.2 1.0
0.18 0.14 0.0
0.76 0.58 1.0
0.4 0.16 1.0
0.98 0.85 0.0
0.42 0.97 1.0
0.75 0.26 1.0
0.24 0.06 1.0
0.97 0.8 0.0
0.21 0.1 2.0
"""
"""
输出：
0 2
"""
import sys
from collections import Counter
input = sys.stdin.readline

def main():
    k, m, n, s = map(int, input().split())

    # 待分类样本 q
    q = list(map(float, input().split()))

    # 读入 m 个样本（n 个特征 + 1 个标签）
    X = []
    y = []
    for _ in range(m):
        row = list(map(float, input().split()))
        X.append(row[:n])
        # 标签以 float 给出，输出需要整数格式
        y.append(int(row[-1]))

    # 计算平方欧氏距离，保存 (dist2, idx)
    dists = []
    for i in range(m):
        xi = X[i]
        # 平方距离即可用于排序
        s2 = 0.0
        for j in range(n):
            diff = q[j] - xi[j]
            s2 += diff * diff
        dists.append((s, i))

    # 按距离升序排序
    dists.sort(key=lambda t: t[0])

    # 取前 k 个邻居的索引与标签
    take = min(k, m)
    top_idx = [dists[i][1] for i in range(take)]
    top_labels = [y[i] for i in top_idx]

    # 统计频次
    cnt = Counter(top_labels)
    max_freq = max(cnt.values())

    # 找出并列第一的标签集合
    tie_labels = {lab for lab, c in cnt.items() if c == max_freq}

    # 若并列，按距离顺序选择第一个属于并列集合的邻居的标签
    # dists 已整体排序，这里只需在前 k 中寻找
    chosen = None
    for i in range(take):
        lab = y[dists[i][1]]
        if lab in tie_labels:
            chosen = lab
            break

    # 输出：标签 与 在前 k 中该标签出现次数
    print(chosen, cnt[chosen])

if __name__ == '__main__':
    main()
