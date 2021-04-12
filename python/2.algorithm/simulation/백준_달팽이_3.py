import sys

# 시간 초과 !!

def solve():
    global n, m

    sx, sy = 0, -1
    nn, nm = n, m

    t = -1
    while True:
        for i in range(4):
            t += 1
            if i == 0 or i == 2:
                for k in range(nm):
                    sy = sy+dy[i]
                nn -= 1
            else:
                for k in range(nn):
                    sx = sx+dx[i]
                nm -= 1

            if nn == 0 or nm == 0:
                print(t)
                print(sx+1, sy+1)
                return



dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
n, m = map(int, sys.stdin.readline().strip().split(" "))
solve()