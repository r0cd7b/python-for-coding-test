# 외벽 점검
from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)

    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    for start in range(length):
        for friends in permutations(dist, len(dist)):
            count = 0
            position = weak[start] + friends[count]
            for index in range(start + 1, start + length):
                if position < weak[index]:
                    count += 1
                    if count >= len(friends):
                        break
                    position = weak[index] + friends[count]
            else:
                answer = min(answer, count + 1)

    if answer <= len(dist):
        return answer
    return -1


print(f"{solution(12, [1, 5, 6, 10], [1, 2, 3, 4])} == 2")
print(f"{solution(12, [1, 3, 4, 9, 10], [3, 5, 7])} == 1")
