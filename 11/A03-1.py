# 문자열 뒤집기 (내 답)
"""
0001100
"""
from sys import stdin

string = stdin.readline()
result = 0
for i in range(len(string) - 2):  # 마지막의 \n 값도 제한하여 범위를 지정한다.
    if string[0] == string[i] and string[0] != string[i + 1]:  # 첫 원소와 동일한 값에서 상반된 값이 등장하는 순간을 센다.
        result += 1
print(result)
