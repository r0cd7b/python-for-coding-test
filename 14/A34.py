# 병사 배치하기
from sys import stdin

n, array = int(stdin.readline()), list(map(int, stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[j] > array[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))

"""
입력 예시
7
15 11 4 8 5 2 4
출력 예시
2
"""
