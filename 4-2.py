# 시각
import sys

n = int(sys.stdin.readline()) + 1

hours = 0
for hour in range(n):
    if hour % 10 == 3:
        hours += 1
# minutes_seconds = 0
# for minute_second in range(60):
#     if minute_second // 10 == 3 or minute_second % 10 == 3:
#         minutes_seconds += 1
cases = n * 1575 + hours * 2025  # n * 60 * 60 - (n - hours) * (60 - minutes_seconds) * (60 - minutes_seconds)

print(cases)
'''
5

11475
'''
