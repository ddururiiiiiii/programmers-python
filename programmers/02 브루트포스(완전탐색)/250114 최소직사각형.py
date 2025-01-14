# https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3
def solution(sizes):
    return max(max(i) for i in sizes) * max(min(i) for i in sizes)