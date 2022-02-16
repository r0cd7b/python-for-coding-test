# 가사 검색
from bisect import bisect_right, bisect_left


def solution(words, queries):
    length, flipped, answer = [[] for _ in range(10000)], [[] for _ in range(10000)], []
    for word in words:
        length_word = len(word) - 2
        length[length_word].append(word)
        flipped[length_word].append(word[::-1])
    for i in range(10000):
        length[i].sort()
        flipped[i].sort()
    for query in queries:
        length_query = len(query) - 2
        if query[0] != '?':
            answer.append(
                bisect_right(
                    length[length_query], query.replace('?', 'z')
                ) - bisect_left(
                    length[length_query], query.replace('?', 'a')
                )
            )
        else:
            query = query[::-1]
            answer.append(
                bisect_right(
                    flipped[length_query], query.replace('?', 'z')
                ) - bisect_left(
                    flipped[length_query], query.replace('?', 'a')
                )
            )
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))  # [3, 2, 4, 1, 0]
