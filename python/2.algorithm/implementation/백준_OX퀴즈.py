import sys


def solve(s):
    ans = 0

    idx = 0
    while True:
        # if s[idx]가 O면 while 시작
        # o 개수를 세고
        # idx가 len(s) 이거나, X면 그만
        # O 개수만큼 계산해서 ans에 더함
        cnt = 0
        while idx < len(s) and s[idx] == 'O':
            cnt += 1
            idx += 1
        ans += cnt*(cnt+1)//2

        if idx == len(s):
            break

        idx += 1

    print(ans)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve(list(sys.stdin.readline().strip()))