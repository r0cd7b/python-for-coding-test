# 외벽 점검
def solution(n, weak, dist):
    dist_week = [(weak[i], weak[i + 1] - weak[i]) for i in range(len(weak) - 1)]
    dist_week.append((weak[-1], n + weak[0] - weak[-1]))

    dist_week.sort(key=lambda i: i[1], reverse=True)

    for i in range(-2, -2 - len(dist), -1):
        for d in dist[:i:-1]:
            pass

    return 0


print(f"{solution(12, [1, 5, 6, 10], [1, 2, 3, 4])} == 2")
print(f"{solution(12, [1, 3, 4, 9, 10], [3, 5, 7])} == 1")

print(f"{solution(12, [1], [1, 2, 3, 4])} == 1")
