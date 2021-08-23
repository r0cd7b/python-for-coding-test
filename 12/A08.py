# 문자열 재정렬
"""
입력 예시 1
K1KA5CB7
출력 예시 1
ABCKK13

입력 예시 2
AJKDLSI412K4JSJ9D
출력 예시 2
ADDIJJJKKLSS20
"""
from sys import stdin

data = stdin.readline().rstrip()

result = []
number = False
value = 0
for x in data:
    if x.isupper():
        result.append(x)
    else:
        number = True
        value += int(x)

result.sort()

if number:
    result.append(str(value))
print(''.join(result))
