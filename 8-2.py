# 1로 만들기
from sys import stdin

x = int(stdin.readline())

minimums = [0] * x
for integer in range(2, x + 1):
    minimum = minimums[integer - 2] + 1
    if not integer % 2:
        compare = minimums[integer // 2 - 1] + 1
        if compare < minimum:
            minimum = compare
    if not integer % 3:
        compare = minimums[integer // 3 - 1] + 1
        if compare < minimum:
            minimum = compare
    if not integer % 5:
        compare = minimums[integer // 5 - 1] + 1
        if compare < minimum:
            minimum = compare
    minimums[integer - 1] = minimum

print(minimums[-1])
