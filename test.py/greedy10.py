import sys

def main():
    m = int(input().strip())
    line = input().strip()
    
    nums = []
    num = 0
    in_num = False
    for c in line:
        if c.isdigit():
            num = num * 10 + int(c)
            in_num = True
        elif in_num:
            nums.append(num)
            num = 0
            in_num = False
    if in_num:
        nums.append(num)
        
    cost = [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]
    
    sumA = sum(a for a, b, in cost)
    diffs = sorted(b - a for a, b in cost)
    extra = sum(diffs[:m//2])
    print(sumA + extra)

if __name__ == "__main__":
    main()