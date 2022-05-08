from collections import deque


def solution(queue1, queue2):
    sum1, sum2, deque1, deque2 = sum(queue1), sum(queue2), deque(queue1), deque(queue2)
    for i in range(len(queue1) + len(queue2)):
        if sum1 == sum2:
            return i
        if sum1 < sum2:
            deque1.append(deque2.popleft())
            sum1, sum2 = sum1 + deque1[-1], sum2 - deque1[-1]
        elif sum1 > sum2:
            deque2.append(deque1.popleft())
            sum1, sum2 = sum1 - deque2[-1], sum2 + deque2[-1]
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]) == 2)
print(solution([1, 2, 1, 2], [1, 10, 1, 2]) == 7)
print(solution([1, 1], [1, 5]) == -1)

# def solution(queue1, queue2):
#     queue, sum1, sum2, start, end = queue1 + queue2, sum(queue1), sum(queue2), 0, len(queue1)
#     for i in range(len(queue)):
#         if sum1 == sum2:
#             return i
#         if sum1 > sum2:
#             sum1, sum2 = sum1 - queue[start], sum2 + queue[start]
#             start = (start + 1) % len(queue)
#         elif sum1 < sum2:
#             sum1, sum2 = sum1 + queue[end], sum2 - queue[end]
#             end = (end + 1) % len(queue)
#     return -1
