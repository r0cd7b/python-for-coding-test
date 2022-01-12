# 카드 정렬하기
from sys import stdin

n = int(stdin.readline())
bundles = sorted([int(stdin.readline()) for _ in range(n)])

if n >= 2:
    number = bundles[0] + bundles[1]
    for i in range(2, n):
        number += number + bundles[i]
else:
    number = bundles[0]

print(number)

"""
입력 예시
3
10
20
40
출력 예시
100
"""
