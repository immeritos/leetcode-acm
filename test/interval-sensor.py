"""
给定按时间戳递增排序的数组sensor_event, 其中每个元素为 [sensor_id, activation_time]。 
定义:第i条记录对应的激活持续时间为当前记录时间戳与上一条记录时间戳之差, 即 di = activation_time(i)- activation_time(i-1), 
其中 activation_time(0)视为实验开始时间0。 
该持续时间归属于当前这一条记录的sensor_id。
要求返回两个sensor_id:
第一个是激活时间 最短 的传感器标识符（若并列取标识符最小者）
第二个是激活时间 最长 的传感器标识符（若并列取标识符最小者）
"""
"""
输入：
6 2
20 4
7 14
10 16
"""
"""
输出：
6 7
"""

import sys
from math import inf

events = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a, b = map(int, line.split())
    events.append((a, b))
    
if not events:
    sys.exit(0)
    
prev = 0
min_dur, max_dur = inf, -inf
min_id, max_id = -1, -1

for sensor_id, t in events:
    dur = t - prev
    if dur < min_dur or (dur == min_dur and sensor_id < min_id):
        min_dur = dur
        min_id = sensor_id
    if dur > max_dur or (dur == max_dur and sensor_id < max_id):
        max_dur = dur
        max_id = sensor_id
    prev = t
    
print(min_id, max_id)