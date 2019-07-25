n = int(input()) 
intervals  = []
for _ in range(n):
    interval = [int(i) for i in input().split()]
    intervals.append(interval)

intervals.sort(key=lambda x: x[0])

best = -1
best_i = -1
for i in range(len(intervals)):
    curr_start, _ = intervals[i]
    count = 0
    for j in range(i):
        if intervals[j][1] < curr_start:
            count += 1
    
    curr = i + 1 - count
    if curr > best:
        best = curr
        best_i = curr_start

print(best_i)