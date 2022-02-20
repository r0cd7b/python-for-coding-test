# 퇴사
from sys import stdin

n, t, p = int(stdin.readline()), [], []
for i in range(n):
    split = stdin.readline().split()
    t.append(int(split[0]))
    p.append(int(split[1]))

if n - 1 + t[-1] > n:
    p[-1] = 0
for i in range(n - 2, -1, -1):
    end, previous = i + t[i], i + 1
    if end < n:
        p[i] = max(p[i] + p[end], p[previous])
    else:
        p[i] = p[previous]

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
