# 외벽 점검
from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)

    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    for start in range(length):

        for friends in permutations(dist, len(dist)):

            position = weak[start] + friends[0]
            for i in range(1, len(friends)):
                for index in range(start + 1, start + length):
                    if position < weak[index]:
                        position = weak[index] + friends[i]
                        break
                else:
                    answer = min(answer, i)

    if answer <= len(dist):
        return answer
    return -1


print(f"{solution(12, [1, 5, 6, 10], [1, 2, 3, 4])} == 2")
print(f"{solution(12, [1, 3, 4, 9, 10], [3, 5, 7])} == 1")
