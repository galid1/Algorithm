import sys

def solve():
    global n, t, d

    cur_d = 0
    board = [[0 for _ in range(n)] for _ in range(n)]
    cx, cy = -1, 0
    start = pow(n, 2)

    # 같은 방향으로 반복 마킹을 하기 위한 변수
    sn = n
    # 방향 전환을 위한 변수
    sn_cnt = 1
    ax, ay = 0, 0
    while start >= 1:
        for i in range(sn):
            cx += d[cur_d][0]
            cy += d[cur_d][1]
            board[cx][cy] = start
            if start == t:
                ax, ay = cx, cy
            start -= 1

        sn_cnt -= 1
        cur_d = switching_d(cur_d)
        if sn_cnt == 0:
            sn_cnt = 2
            sn -= 1

    # 정답
    for row in board:
        for c in row:
            print(c, end=' ')
        print()
    print(ax+1, ay+1)

def switching_d(cur_d):
    return (cur_d + 1)%4


d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(sys.stdin.readline().strip())
t = int(sys.stdin.readline().strip())
solve()