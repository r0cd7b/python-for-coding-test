# 외벽 점검
from itertools import permutations


def solution(n, weak, dist):
    for number in range(1, len(dist) + 1):
        for permutation in permutations(dist, number):

            for index_first in range(len(weak)):
                location = weak[index_first]
                index = index_first
                for distance in permutation:
                    for _ in range(distance + 1):
                        if location == weak[index]:
                            index = (index + 1) % len(weak)
                            if index == index_first:
                                return len(permutation)
                        location = (location + 1) % n

    return -1


print(f"{solution(12, [1, 5, 6, 10], [1, 2, 3, 4])} == 2")
print(f"{solution(12, [1, 3, 4, 9, 10], [3, 5, 7])} == 1")
