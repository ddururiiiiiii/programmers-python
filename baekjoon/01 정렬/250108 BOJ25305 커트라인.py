# https://www.acmicpc.net/problem/25305
arr = list(map(int, (input().split(" "))))
n, limit = arr[0], arr[1]
score = list(map(int, input().split(" ")))
score.sort(reverse=True)
print(score[limit-1])