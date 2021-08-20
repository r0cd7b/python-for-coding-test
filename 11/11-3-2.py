# 문자열 뒤집기 (책 답)
"""
0001100
"""
from sys import stdin

data = stdin.readline()
count0 = 0
count1 = 0
if data[0] == '0':
    count1 += 1
else:
    count0 += 1
for i in range(len(data) - 2):
    next_i = i + 1
    if data[i] != data[next_i]:
        if data[next_i] == '0':
            count1 += 1
        else:
            count0 += 1
print(min(count0, count1))
