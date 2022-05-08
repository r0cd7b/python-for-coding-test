from collections import deque


def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    minimum = -1
    for i in range(len(deque1)):
        deque3 = deque(deque1)
        deque4 = deque(deque2)
        for j in range(len(deque2)):
            print(deque3)
            print(deque4)
            print()
            if sum(deque3) == sum(deque4):
                number = i + j
                if not (number >= minimum >= 0):
                    minimum = number
            deque3.append(deque4.popleft())
        deque2.append(deque1.popleft())
    return minimum


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
