# 위에서 아래로
"""
3
15
27
12
"""
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort(reverse=True)
for i in array:
    print(i, end=' ')
