# 병사 배치하기
from sys import stdin

n, soldiers = int(stdin.readline()), list(map(int, stdin.readline().split()))
sequences = [1] * n

for i in range(1, n):
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            sequences[i] = max(sequences[j] + 1, sequences[i])

print(n - max(sequences))

"""
입력 예시
7
15 11 4 8 5 2 4
출력 예시
2
"""
