import sys

def solution(sx, sy, d):
    global b, r, c, max_num, dx, dy

    for i in range(4):
        nx, ny = sx+dx[i], sy+dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if not v[ord(b[nx][ny]) - 65]:
                v[ord(b[nx][ny]) - 65] = 1
                solution(nx, ny, d + 1)
                v[ord(b[nx][ny]) - 65] = 0

    max_num = max(max_num, d)


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
v = [0 for i in range(26)]
max_num = 0
r, c = map(int, sys.stdin.readline().split(" "))
b = []
for i in range(r):
    b.append(list(sys.stdin.readline().strip()))
# 0,0 방문 표시
v[ord(b[0][0])-65] = 1

solution(0, 0, 1)
print(max_num)