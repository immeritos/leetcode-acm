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