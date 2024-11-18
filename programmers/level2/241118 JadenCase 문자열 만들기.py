# capitalize()
# - 단어의 경우 첫번째 알파벳만 대문자로 전환
# - 문장의 경우 문장의 가장 첫 단어만 전환함
# - 앞에 숫자가 있는 경우 그대로 반환
# ex) 'hi' -> 'Hi'
# ex) 'hi, seulgi?' -> 'Hi, seulgi'
# ex) '3hi' -> '3hi'
def solution(s):
    answer = ''
    arr = s.split(' ')
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    answer = ' '.join(arr)
    return answer