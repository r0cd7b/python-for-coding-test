# 무지의 먹방 라이브
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    length = len(food_times)
    previous = 0
    while k >= length * (q[0][0] - previous):
        now = heapq.heappop(q)[0]
        k -= length * (now - previous)
        length -= 1
        previous = now

    return sorted(q, key=lambda x: x[1])[k % length][1]


print(f"{solution([3, 1, 2], 5)}: 1")
print(f"{solution([8, 6, 4], 15)}: 2")
