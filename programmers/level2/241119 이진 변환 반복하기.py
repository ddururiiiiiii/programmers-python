def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1 # 이진 변환 횟수
        num = s.count("1")
        b += s.count("0") # 0의 갯수
        s = bin(num)[2:]
    return [a, b]