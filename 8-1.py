# 다이나믹 프로그래밍
d = [1, 1] + [0] * 98
n = 99

for i in range(2, n):
    d[i] = d[i - 2] + d[i - 1]

print(d[n - 1])
