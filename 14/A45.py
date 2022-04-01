# 최종 순위
from sys import stdin

n = int(stdin.readline())
for _ in range(n):
    t = list(map(int, stdin.readline().split()))

"""
입력 예시
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
출력 예시
5 3 2 4 1
2 3 1
IMPOSSIBLE
"""
