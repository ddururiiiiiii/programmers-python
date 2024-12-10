# 오답
def solution(numbers):
    answer = []
    arr = numbers

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                break;
        if (i+1) != len(answer):
            answer.append(-1)
    return answer

# 정답
def solution2(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer