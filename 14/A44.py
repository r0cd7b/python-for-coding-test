# 행성 터널
from sys import stdin

n, planets = int(stdin.readline()), []
for i in range(n):
    x, y, z = map(int, stdin.readline().split())
    planets.append((i, x, y, z))
print(planets, end="\n\n")
tunnels = []
for i in range(1, 4):
    planets.sort(key=lambda p: p[i])
    print(planets)
    for j in range(n - 1):
        next_ = j + 1
        tunnels.append((abs(planets[j][i] - planets[next_][i]), planets[j][0], planets[next_][0]))
    print(tunnels, end="\n\n")

"""
입력 예시
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
출력 예시
4
"""
