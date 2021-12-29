# 안테나
from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))

data.sort()

print(data[(n - 1) // 2])

"""
입력 예시
4
5 1 7 9
출력 예시
5
"""
