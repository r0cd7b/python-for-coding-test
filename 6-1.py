# 위에서 아래로
from sys import stdin

sequence = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
sequence.sort(reverse=True)
for number in sequence:
    print(number, end=' ')
'''
3
15
27
12

27 15 12
'''
