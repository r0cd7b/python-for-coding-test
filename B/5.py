# 투 포인터
a, b, i, j = [1, 3, 5], [2, 4, 6, 8], 0, 0
result = []
for _ in range(len(a) + len(b)):
    if i >= len(a):
        result.append(b[j])
    elif j >= len(b):
        result.append(a[i])
    elif a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1
for i in result:
    print(i, end=' ')
