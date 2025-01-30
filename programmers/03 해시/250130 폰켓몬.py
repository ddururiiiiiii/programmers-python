# https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    answer = 0

    mari = len(nums) // 2

    if len(set(nums)) >= mari:
        return mari
    else:
        return len(set(nums))


    return answer