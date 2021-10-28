# 외벽 점검
def solution(n, weak, dist):
    if n <= 2:
        return 1

    wall_condition = [0] * n
    for i in weak:
        wall_condition[i] = 1
    print(wall_condition)

    two_weaks = [((weak[(i + 1) % len(weak)] - weak[i]) % n, i) for i in range(len(weak))]
    print(two_weaks)
    two_weaks.sort(reverse=True)
    print(two_weaks)

    return -1


print(f"{solution(12, [1, 5, 6, 10], [1, 2, 3, 4])} == 2\n")
print(f"{solution(12, [1, 3, 4, 9, 10], [3, 5, 7])} == 1")
