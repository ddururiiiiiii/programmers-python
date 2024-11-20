def solution(n):
    answer = n
    while True:
        answer += 1
        if bin(answer)[2:].count("1") == bin(n)[2:].count("1"):
            return answer
    return answer