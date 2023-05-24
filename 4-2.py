# 시각
import sys

n = int(sys.stdin.readline()) + 1

hours = 0
for hour in range(n):
    if hour % 10 == 3:
        hours += 1
# minutes_seconds = 15 = 6 * 10 - (6 - 1) * (10 - 1)
cases = n * 1575 + hours * 2025  # = n * 60 * 60 - (n - hours) * (60 - minutes_seconds) * (60 - minutes_seconds)

print(cases)
'''
5

11475
'''
