# 탑승구
from sys import stdin

G, P = int(stdin.readline()), int(stdin.readline())
g, conditions = [int(stdin.readline()) - 1 for _ in range(P)], [0] * G
for i in range(1, P + 1):
    if conditions.count(i - 1) < 2:
        print(i)
        break
    for j in range(g[i] + 1):
        conditions[j] = i

"""
입력 예시
4
3
4
1
1
출력 예시
2
"""
