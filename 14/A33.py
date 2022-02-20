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
입력 예시 1
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
출력 예시 1
45

입력 예시 2
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
출력 예시 2
55

입력 예시 3
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6
출력 예시 3
20

입력 예시 4
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
출력 예시 4
90
"""
