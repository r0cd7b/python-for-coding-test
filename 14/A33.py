# 퇴사
from sys import stdin

n, t, p = int(stdin.readline()), [], []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    t.append(x)
    p.append(y)

p.append(0)
for i in range(n - 1, -1, -1):
    time, max_value = t[i] + i, p[i + 1]
    if time <= n:
        p[i] = max(p[i] + p[time], max_value)
    else:
        p[i] = max_value

print(p[0])

"""
입력 예시
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
출력 예시
45

입력 예시
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
출력 예시
55
"""
