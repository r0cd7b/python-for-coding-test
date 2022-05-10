# 암호 만들기
from sys import stdin
from itertools import combinations

(L, C), characters, vowels = \
    map(int, stdin.readline().split()), sorted(stdin.readline().split()), {'a', 'e', 'i', 'o', 'u'}
for combination in combinations(characters, L):
    number_vowels, number_consonants = 0, 0
    for character in combination:
        if character in vowels:
            number_vowels += 1
        else:
            number_consonants += 1
        if number_vowels >= 1 and number_consonants >= 2:
            break
    else:
        continue
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
istw
"""
