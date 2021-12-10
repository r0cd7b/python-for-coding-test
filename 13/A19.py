# 연산자 끼워 넣기
from sys import stdin


def dfs(i, now):
    global add, sub, mul, div, max_value, min_value
    if i == n:
        max_value, min_value = max(max_value, now), min(min_value, now)
        return
    if add:
        add -= 1
        dfs(i + 1, now + data[i])
        add += 1
    if sub:
        sub -= 1
        dfs(i + 1, now - data[i])
        sub += 1
    if mul:
        mul -= 1
        dfs(i + 1, now * data[i])
        mul += 1
    if div:
        div -= 1
        dfs(i + 1, int(now / data[i]))
        div += 1


n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
add, sub, mul, div = map(int, stdin.readline().split())

max_value, min_value = -1e9, 1e9
dfs(1, data[0])

print(max_value)
print(min_value)

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
