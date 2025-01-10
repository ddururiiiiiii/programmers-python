# https://www.acmicpc.net/problem/1182
import itertools
N, num = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    for j in itertools.combinations(arr, i+1):
        if num == sum(j):
            cnt += 1
print(cnt)