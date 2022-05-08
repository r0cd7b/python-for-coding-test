# 투 포인터
data, m = [1, 2, 3, 2, 5], 5
start, end, difference, count = 0, 0, data[0] - m, 0
while start < len(data) > end:
    if difference == 0:
        count += 1
    if difference >= 0:
        difference -= data[start]
        start += 1
    elif difference < 0:
        end += 1
        difference += data[end]
print(count)
