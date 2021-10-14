import sys


def solve(ci):
    global n, m, board, bits, ans

    if ci == n*m:
        ans = max(ans, cal())
        return

    bits[ci] = 1
    solve(ci+1)

    bits[ci] = 0
    solve(ci+1)


def cal():
    global board, bits, n, m

    result = 0
    visited = [False for _ in range(n*m)]
    for i in range(n*m):
        if visited[i]:
            continue

        num = ''
        cr = i//m
        ti = i

        if bits[i] == 1:
            while cr == (ti//m) and bits[ti] == 1:
                num += board[cr][ti%m]
                visited[ti] = True
                ti += 1

        else:
            while ti//m < n and bits[ti] == 0:
                num += board[ti//m][ti%m]
                visited[ti] = True
                ti += m

        if not num:
            continue

        result += int(num)

    return result


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []

for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

bits = [0 for _ in range(n*m)]
ans = 0
solve(0)
print(ans)