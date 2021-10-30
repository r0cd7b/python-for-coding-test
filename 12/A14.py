# 외벽 점검
def solution(n, weak, dist):
    point = 0
    for i in range(-2, -(len(dist) + 2), -1):
        print(dist[-1:i:-1])
        for dist_check in dist[-1:i:-1]:
            pass

    return -1


print(f"{solution(12, [1, 5, 6, 10], [1, 2, 3, 4])} == 2")
print(f"{solution(12, [1, 3, 4, 9, 10], [3, 5, 7])} == 1")
