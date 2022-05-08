from collections import deque


def solution(queue1, queue2):
    difference = sum(queue1) - sum(queue2)
    if difference == 0:
        return 0
    deque1, deque2 = deque(queue1), deque(queue2)
    for i in range(1, len(deque1) + len(deque2)):
        if difference < 0:
            deque1.append(deque2.popleft())
            difference += deque1[-1] * 2
        elif difference > 0:
            deque2.append(deque1.popleft())
            difference -= deque2[-1] * 2
        if difference == 0:
            return i
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))  # 7
print(solution([1, 1], [1, 5]))  # -1

# def solution(queue1, queue2):
#     difference = sum(queue1) - sum(queue2)
#     if difference == 0:
#         return 0
#     queue, start, end = queue1 + queue2, 0, len(queue1)
#     for i in range(1, len(queue)):
#         if difference > 0:
#             difference -= queue[start] * 2
#             start = (start + 1) % len(queue)
#         elif difference < 0:
#             difference += queue[end] * 2
#             end = (end + 1) % len(queue)
#         if difference == 0:
#             return i
#     return -1
