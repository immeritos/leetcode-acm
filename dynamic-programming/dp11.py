N = int(input())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))
    
box.sort(key=lambda x:(x[0], x[1], x[2]))

dp = [0] * N

for i in range(N):
    dp[i] = box[i][2]
    for j in range(i):
        if box[i][0]>box[j][0] and box[i][1]>box[j][1] and box[i][2]>box[j][2]:
            dp[i] = max(dp[i], dp[j] + box[i][2])
            
print(max(dp))