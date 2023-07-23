# 부품 찾기
from sys import stdin

stdin.readline()
parts = set(stdin.readline().split())
stdin.readline()
for part in stdin.readline().split():
    if part in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')

'''
5
8 3 7 9 2
3
5 7 9

no yes yes
'''
