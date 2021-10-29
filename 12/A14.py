# 외벽 점검
def solution(n, weak, dist):
    if n <= 2:
        return 1

    data_two_weaks = []
    for i in range(len(weak)):
        next_i = (i + 1) % len(weak)
        data_two_weaks.append(((weak[next_i] - weak[i]) % n, i, next_i))
    data_two_weaks.sort(reverse=True)

    walls_excluded = []
    for i in range(len(dist) - 1):
        walls_excluded.append(data_two_weaks[i])
        walls_excluded.sort(key=lambda d: d[1])

        dists_check = []
        for j in range(len(walls_excluded)):
            dists_check.append(
                (weak[walls_excluded[(j + 1) % len(walls_excluded)][1]] - weak[walls_excluded[j][2]]) % n)
        dists_check.sort(reverse=True)

        for j in range(len(dists_check)):
            if dists_check[j] > dist[-j - 1]:
                break
        else:
            return len(dists_check)

    return -1


print(f"{solution(12, [1, 5, 6, 10], [1, 2, 3, 4])} == 2")
print(f"{solution(12, [1, 3, 4, 9, 10], [3, 5, 7])} == 1")
