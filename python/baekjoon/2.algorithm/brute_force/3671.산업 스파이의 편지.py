import sys

def solve(cur, length):
    global board, ps, ans, visited, selected

    if len(cur) == length:
        num = int(cur)
        if board[num] and num not in visited:
            visited.add(num)
            ans += 1
        return

    for i in range(len(ps)):
        if selected[i]:
            continue

        selected[i] = True
        solve(cur + str(ps[i]), length)
        selected[i] = False


def make_board():
    MAX = 10_000_000
    board = [True for _ in range(MAX + 1)]
    board[0], board[1] = False, False

    for i in range(2, MAX):
        if not board[i]:
            continue

        for num in range(i+i, MAX, i):
            board[num] = False

    return board


board = make_board()
t = int(sys.stdin.readline().strip())
selected = [False for _ in range(10)]
for _ in range(t):
    ps = list(map(int, sys.stdin.readline().strip()))
    visited = set()
    ans = 0
    for length in range(1, len(ps)+1):
        solve('', length)
    print(ans)
