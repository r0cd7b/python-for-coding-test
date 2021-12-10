# 연산자 끼워 넣기
from sys import stdin
from itertools import permutations

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
operators = list(map(int, stdin.readline().split()))

operators, maximum, minimum = ['+'] * operators[0] + ['-'] * operators[1] + ['*'] * operators[2] + ['//'] * operators[
    3], -1e9, 1e9
for permutation in permutations(operators, len(operators)):
    result = a[0]
    for a_index in range(1, len(a)):
        permutation_index = a_index - 1
        if permutation[permutation_index] == '+':
            result += a[a_index]
        elif permutation[permutation_index] == '-':
            result -= a[a_index]
        elif permutation[permutation_index] == '*':
            result *= a[a_index]
        elif result >= 0:
            result //= a[a_index]
        else:
            result = -(-result // a[a_index])
    maximum, minimum = max(maximum, result), min(minimum, result)
print(maximum)
print(minimum)

"""
입력 예시 1
2
5 6
0 0 1 0
출력 예시 1
30
30

입력 예시 2
3
3 4 5
1 0 1 0
출력 예시 2
35
17

입력 예시 3
6
1 2 3 4 5 6
2 1 1 1
출력 예시 3
54
-24
"""
