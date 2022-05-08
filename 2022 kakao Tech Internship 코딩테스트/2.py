from collections import deque


def solution(queue1, queue2):
    deque1, deque2 = deque(queue1), deque(queue2)
    for i in range(len(deque1) + len(deque2)):
        sum1, sum2 = sum(deque1), sum(deque2)
        if sum1 == sum2:
            return i
        if sum1 < sum2:
            deque1.append(deque2.popleft())
        elif sum1 > sum2:
            deque2.append(deque1.popleft())
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]) == 2)
print(solution([1, 2, 1, 2], [1, 10, 1, 2]) == 7)
print(solution([1, 1], [1, 5]) == -1)
