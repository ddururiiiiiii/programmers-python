# https://www.acmicpc.net/problem/25305
# arr = list(map(int, (input().split(" "))))
# n, limit = arr[0], arr[1]
# score = list(map(int, input().split(" ")))
# score.sort(reverse=True)
# print(score[limit-1])

tmp = list(map(int, input().split(" ")))
n, limit = tmp[0], tmp[1]
arr = sorted(list(map(int, input().split(" "))), reverse=True)
print(arr[limit-1])