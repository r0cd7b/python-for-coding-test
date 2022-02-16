# 가사 검색
from bisect import bisect_right, bisect_left


def count_by_range(a, left_value, right_value):
    return bisect_right(a, right_value) - bisect_left(a, left_value)


array = [[] for _ in range(10000)]
reversed_array = [[] for _ in range(10000)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word) - 2].append(word)
        reversed_array[len(word) - 2].append(word)
    for i in range(10000):
        array[i].sort()
        reversed_array[i].sort()
    for q in queries:
        if q[0] != '?':
            answer.append(count_by_range(array[len(q) - 2], q.replace('?', 'a'), q.replace('?', 'z')))
        else:
            q = q[::-1]
            answer.append(count_by_range(array[len(q) - 2], q.replace('?', 'a'), q.replace('?', 'z')))
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))  # [3, 2, 4, 1, 0]
