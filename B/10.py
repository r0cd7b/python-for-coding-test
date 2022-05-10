# 암호 만들기
from sys import stdin
from itertools import combinations

L, C = map(int, stdin.readline().split())
characters = sorted(stdin.readline().split())
for combination in combinations(characters, L):
    print(''.join(combination))

"""
입력 예시
4 6
a t c i s w
출력 예시
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
cstw
istw
"""
