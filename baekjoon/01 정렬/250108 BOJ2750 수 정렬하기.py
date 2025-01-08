# https://www.acmicpc.net/problem/2750
n = int(input())
infos = [ int(input()) for _ in range(n)]
infos.sort()
for i in infos:
    print(i)
