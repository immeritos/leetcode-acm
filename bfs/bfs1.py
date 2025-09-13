from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)

pritn("队列大小：", len(q))

print("队列头部元素：", q[0])

q.popleft()

print("新的队列头部元素：", q[0])

if len(q) == 0:
    print("队列为空")
else:
    print("队列不为空")