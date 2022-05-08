def solution(alp, cop, problems):
    answer = 0

    max_alp_reqs = max([problem[0] for problem in problems])
    max_cop_reqs = max([problem[1] for problem in problems])
    while alp < max_alp_reqs or cop < max_cop_reqs:

        solvable_problems = [
            [problem[2], problem[3], problem[4]] for problem in problems if alp >= problem[0] and cop >= problem[1]
        ]

        reach_problems = [
            problem
            for problem in solvable_problems
            if max_alp_reqs <= alp + problem[0] and max_cop_reqs <= cop + problem[1]
        ]
        if reach_problems:
            return min([problem[4] for problem in reach_problems])

    return answer


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
