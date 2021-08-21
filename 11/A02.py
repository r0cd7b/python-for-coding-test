# 곱하기 혹은 더하기
"""
02984

576
"""
from sys import stdin

data = stdin.readline().strip()
result = 0
for i in data:
    num = int(i)
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
print(result)
