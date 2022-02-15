# 가사 검색
from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []

    length, flipped = [[] for _ in range(10000)], [[] for _ in range(10000)]
    for word in words:
        length[len(word) - 2].append(word)
        flipped[len(word) - 2].append(word[::-1])
    for i in range(10000):
        length[i].sort()
        flipped[i].sort()
    for query in queries:
        if query[0] != '?':
            answer.append(
                bisect_right(length[len(query) - 2], query.replace('?', 'z')) - bisect_left(length[len(query) - 2],
                                                                                            query.replace('?', 'a')))
        else:
            query = query[::-1]
            answer.append(
                bisect_right(flipped[len(query) - 2], query.replace('?', 'z')) - bisect_left(flipped[len(query) - 2],
                                                                                             query.replace('?', 'a')))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))  # [3, 2, 4, 1, 0]
