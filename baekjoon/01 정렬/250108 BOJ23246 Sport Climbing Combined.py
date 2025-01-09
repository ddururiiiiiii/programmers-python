# https://www.acmicpc.net/problem/23246
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))
for a, b, c, b in arr[:3]:
    print(a, end=" ")
