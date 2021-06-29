# 큐
from collections import deque

queue = deque()
queue.appendleft(5)
queue.appendleft(2)
queue.appendleft(3)
queue.appendleft(7)
queue.pop()
queue.appendleft(1)
queue.appendleft(4)
queue.pop()
print(queue)
