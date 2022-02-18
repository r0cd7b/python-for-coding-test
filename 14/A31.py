# 금광
from sys import stdin

sizes = []
for _ in range(int(stdin.readline())):
    (n, m), array = map(int, stdin.readline().split()), list(map(int, stdin.readline().split()))

    for i in range(1, m):
        for j in range(n):
            left, up, down = i - 1, j - 1, j + 1
            array[j * m + i] += max(array[j * m + left], array[up * m + left] if up >= 0 else 0,
                                    array[down * m + left] if down < n - 1 else 0)
    m_max = m - 1
    result = array[m_max]
    for i in range(1, n):
        result = max(array[i * m + m_max], result)
    sizes.append(result)

for size in sizes:
    print(size)

"""
입력 예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
출력 예시
19
16
"""
