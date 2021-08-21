# 모험가 길드
"""
5
2 3 1 2 2
"""
from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
data.sort()
count = 0
result = 0
for i in data:
    count += 1
    if count >= i:
        count = 0
        result += 1
print(result)
