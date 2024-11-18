def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for idx, v in enumerate(A):
        answer += v * B[idx]
    return answer