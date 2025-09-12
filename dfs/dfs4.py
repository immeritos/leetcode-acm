def dfs(nums, path, visited, result):
    if len(path) == len(nums):
        result.append(path[:])
        return
    
    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            path.append(nums[i])
            dfs(nums, path, visted, result)
            path.pop()
            visited[i] = False
            
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    
    nums.sort()
    
    result = []
    path = []
    visited = [False]
    
    dfs(nums, path, visited, result)
    
    for perm in result:
        print(" ".join(map(str, perm)))
        
if __name__ == "__main__":
    main()