# 신고 결과 받기
def solution(id_list, report, k):
    numbers = [set() for _ in range(len(id_list))]
    ids = {id_list[i]: i for i in range(len(id_list))}
    for r in report:
        user1, user2 = r.split()
        numbers[ids[user2]].add(ids[user1])

    answer = [0] * len(id_list)
    for reported in numbers:
        if len(reported) >= k:
            for id_ in reported:
                answer[id_] += 1
    return answer


print(
    solution(
        ["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2
    )
)  # [2, 1, 1, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))  # [0, 0]
