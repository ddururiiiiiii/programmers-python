# https://www.acmicpc.net/problem/2503
import itertools
N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
cnt = 0
for ans in itertools.permutations(range(1, 10), 3):
    ok = True
    for num, a, b in arr:
        stk = bal = 0

        for i in range(3):
            if str(ans[i]) == num[i] :
                stk += 1
            elif str(ans[i]) in num :
                bal += 1
        if stk != int(a) or bal != int(b):
            ok = False
            break

    if ok : cnt += 1
print(cnt)
