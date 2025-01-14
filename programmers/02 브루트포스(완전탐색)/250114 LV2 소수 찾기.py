# https://school.programmers.co.kr/learn/courses/30/lessons/42839

import math
from itertools import permutations
def sosu_chk(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
    return True

def solution(numbers):
    answer = 0
    arr = []
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            arr.append(''.join(map(str, list(j))))
    arr = list(set(map(int, arr)))

    for i in arr:
        if sosu_chk(i):
            answer += 1

    return answer