# https://www.acmicpc.net/problem/2798
import itertools
N , num = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = []
for i in itertools.permutations(arr, 3):
    if sum(i) <= num:
        arr2.append(sum(i))
print(max(arr2))