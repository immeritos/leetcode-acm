"""
Design a program to solve a specific array analysis problem.

Given an array of non-negative integers arr, 
where each integer has a "weight" represented by the sum of the digits in its hexadecimal representation 
(the weight is calculated based on the sum of each digit in the hexadecimal representation, 
with weights 0 through 9 representing weights 0 through 9, 
and weights A: 10, B: 11, C: 12, D: 13, E: 14, and F: 15).

Your task is to find the first element with a greater "weight" to the right of each element in the array,
and return a new array containing the indices of these elements.

If there is no element with a greater "weight" to the right of an element, return -1 for that position.
"""

def compute_weight(n):
    """计算整数 n 的十六进制表示中各位数字的和"""
    if n == 0:
        return 0
    s = 0
    while n > 0:
        # digit = n & 0xF
        # - 0xF = 十六进制 F = 二进制 1111 = 十进制 15
        # - 按位与 &：会把 n 和 0xF 转成二进制并逐位比较
        #   只保留 n 的最低四位（因为 0xF = 0000 1111）
        # - 相当于取出 n 的“最后一位十六进制数”的数值
        digit = n & 0xF
        
        # 加到权重和中
        # 注意：digit 已经是整数值，不论原来是十进制写法还是十六进制写法，
        # Python 内部存储的都是数值，所以这里直接做加法
        s += digit

        # n >>= 4
        # - 右移 4 位，相当于除以 16（去掉已经处理过的最低一位十六进制数）
        # - 因为每 1 个十六进制位 = 4 个二进制位
        n >>= 4
    return s

def main():
    import sys
    N = int(input())
    
    arr = list(map(int, input().split()))
    
    # 预先计算每个数的十六进制权重
    weights = [compute_weight(num) for num in arr]
    
    answer = [-1] * N 
    
    stack = []
    
    # 从右向左遍历，维护单调栈
    for i in range(N-1, -1, -1):
        # 弹出不大于当前权重的下标
        while stack and weights[stack[-1]] <= weights[i]:
            stack.pop()
        
        # 如果栈不空，栈顶元素就是右侧第一个比当前权重大的元素下标
        if stack:
            answer[i] = stack[-1]
        else:
            answer[i] = -1
            
        # 当前下标入栈
        stack.append(i)
    
    # 输出结果，空格分隔
    print(' '.join(map(str, answer)))
    
if __name__ == "__main__":
    main()