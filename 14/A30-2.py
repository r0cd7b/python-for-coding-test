# 가사 검색
def solution(words, queries):
    answer = []

    length = [[] for _ in range(10000)]
    for word in words:
        length[len(word) - 2].append(word)
    for query in queries:
        result = 0
        for word in length[len(query) - 2]:
            for i in range(len(query)):
                if query[i] != word[i] and query[i] != '?':
                    break
            else:
                result += 1
        answer.append(result)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))  # [3, 2, 4, 1, 0]
