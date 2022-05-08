# 투 포인터
n = m = 5
data = [1, 2, 3, 2, 5]
count = interval_sum = end = 0
for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
print(count)

count = 0

data, start, end = [1, 2, 3, 2, 5], 0, 1
m = 5
difference = m - data[0]
while start < end < len(data):
    if difference > 0:
        difference, end = difference - data[end], end + 1
    elif difference < 0:
        difference, start = difference + data[start], start + 1
    if difference == 0:
        count += 1
print(count)
