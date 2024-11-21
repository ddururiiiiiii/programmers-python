def solution(s):
    stack = []

    for i in range(len(s)):
        # stack이 비어있으면
        if len(stack) == 0 :
            stack.append(s[i])
        # stack의 마지막 문자가 현재 문자와 같으면
        elif stack[-1] == s[i] :
            stack.pop()
        # stack의 마지막 문자가 현재 문자와 같지 않다면
        else:
            stack.append(s[i])

    # stack에 남아있는 문자가 없다면
    if len(stack) == 0 :
        return 1

    return 0