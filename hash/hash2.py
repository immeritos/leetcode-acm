from collections import defaultdict

def main():
    positions = defaultdict(list)
    
    # 示例数据
    a = [1, 2, 3, 2, 1, 2, 3, 2]
    
    # 遍历数组，记录每个数字出现的位置（从1开始计数）
    for i in range(len(a)):
        positions[a[i]].append(i + 1)
    
    # 输出 positions
    for key, value in positions.items():
        print(f"数字 {key} 出现的位置: {' '.join(map(str, value))}")

if __name__ == "__main__":
    main()
