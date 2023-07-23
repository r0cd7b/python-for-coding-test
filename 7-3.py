# 떡볶이 떡 만들기
from sys import stdin

n, m = stdin.readline().split()
n, m = int(n), int(m)
heights = list(map(int, stdin.readline().split()))

start, end, maximum = 0, max(heights), 0
while start <= end:
    mid, total = (start + end) // 2, 0
    for height in heights:
        cut = height - mid
        if cut > 0:
            total += cut
    if m == total:
        maximum = mid
        break
    if m < total:
        start, maximum = mid + 1, mid
    else:
        end = mid - 1

print(maximum)
'''
4 6
19 15 10 17

15
'''
