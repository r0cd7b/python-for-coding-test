# 외벽 점검
def solution(n, weak, dist):
    if n <= 2:
        return 1

    dist_between_two_weaks = [(weak[i + 1] - weak[i], weak[i]) for i in range(len(weak) - 1)]
    dist_between_two_weaks.append((n - weak[-1] + weak[0], weak[-1]))
    dist_between_two_weaks.sort(reverse=True)
    print(dist_between_two_weaks)

    for number_of_people in range(len(dist)):
        pass

    return -1


print(f"{solution(12, [1, 5, 6, 10], [1, 2, 3, 4])} == 2")
print(f"{solution(12, [1, 3, 4, 9, 10], [3, 5, 7])} == 1")

print(f"{solution(3, [0, 1, 2], [3, 5, 7])} == 1")
