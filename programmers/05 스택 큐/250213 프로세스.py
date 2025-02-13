# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([ (value, idx) for idx, value in enumerate(priorities)])
    print_order = 0

    while queue:
        current = queue.popleft()

        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[1] == location:
                return print_order

    return answer