# https://www.acmicpc.net/problem/10814
N = int(input())
arr = sorted([list(input().split()) for _ in range(N)], key=lambda x:int(x[0]))
for a, b in arr:
    print(a, b)
