import sys


def solve():
    global n, ans

    for digit in range(1, 11):
        dfs(digit, '', '')

        if ans:
            break


def dfs(digit, cur, bef):
    global r, ans

    if r == -1:
        return

    if len(cur) == digit:
        r -= 1
        if r == 0:
            ans = cur
        return

    for i in range(10):
        if bef == '':
            dfs(digit, cur+str(i), i)
        else:
            if i < bef:
                dfs(digit, cur+str(i), i)
            else:
                break


n = int(sys.stdin.readline().strip())
if n > 1023:
    print(-1)
else:
    r = n
    ans = ''
    solve()
    print(ans)



