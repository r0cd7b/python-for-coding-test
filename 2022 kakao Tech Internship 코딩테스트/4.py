from collections import deque
from copy import deepcopy


def solution(n, paths, gates, summits):
    nodes: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        nodes[i].append((j, w))
        nodes[j].append((i, w))

    gates = deque(gates)
    summits = deque(summits)

    answer = [0, 10000001]
    for _ in range(len(gates)):
        gate = gates.popleft()
        other_gates = {g for g in gates}

        for _ in range(len(summits)):
            summit = summits.popleft()
            other_summits = {s for s in summits}

            visit = [False] * (n + 1)
            visit[gate] = True
            stack = [(gate, 0, visit)]
            while stack:
                i, intensity, visit = stack.pop()
                if intensity <= answer[1]:
                    if i == summit:
                        if intensity < answer[1] or intensity == answer[1] and summit < answer[0]:
                            answer[0] = summit
                            answer[1] = intensity
                    else:
                        for j, w in nodes[i]:
                            if not visit[j] and j not in other_gates and j not in other_summits:
                                new_visit = deepcopy(visit)
                                new_visit[j] = True
                                stack.append((j, max(intensity, w), new_visit))

            summits.append(summit)
        gates.append(gate)
    return answer


print(solution(
    6,
    [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
    [1, 3],
    [5]
))
print(solution(
    7,
    [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
    [1],
    [2, 3, 4]
))
print(solution(
    7,
    [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
    [3, 7],
    [1, 5]
))
print(solution(
    5,
    [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],
    [1, 2],
    [5]
))
