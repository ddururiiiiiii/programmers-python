def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j] :
                answer[i] = j-i
                break;

        if answer[i] == 0:
            answer[i] = len(prices)-i-1

    return answer