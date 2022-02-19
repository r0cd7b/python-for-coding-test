# 정수 삼각형
from sys import stdin

n = int(stdin.readline())
dp = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(dp[i])):
        up, left = i - 1, j - 1
        dp[i][j] += max(dp[up][left] if left >= 0 else 0, dp[up][j] if j < len(dp[up]) else 0)

print(max(dp[-1]))

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
