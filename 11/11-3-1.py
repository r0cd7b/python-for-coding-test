# 문자열 뒤집기 (내 답)
"""
0001100
"""
from sys import stdin

data = stdin.readline()
result = 0
for i in range(len(data) - 2):
    if data[0] == data[i] and data[0] != data[i + 1]:  # 첫 원소와 동일한 값에서 상반된 값이 등장하는 순간을 센다.
        result += 1
print(result)
