# 정수 삼각형
from sys import stdin

n = int(stdin.readline())
triangle = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(triangle[i])):
        previous_i, previous_j = i - 1, j - 1
        triangle[i][j] += max(triangle[previous_i][previous_j] if previous_j >= 0 else 0,
                              triangle[previous_i][j] if j < len(triangle[previous_i]) else 0)

print(max(triangle[-1]))

"""
입력 예시
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
출력 예시
30
"""
