# https://school.programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product
def solution(word):
    answer = 0
    arr = 'AEIOU'
    word_list = []
    for i in range(1, 6):
        for w in product(arr, repeat = i):
            word_list.append(''.join(list(w)))

    word_list.sort()

    return word_list.index(word) + 1 