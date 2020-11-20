import sys

def solution():
    global w, h, lands
    answer = 0
    v = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if lands[i][j] != 0 and v[i][j] == 0:
                answer += 1
                stack = [(i, j)]
                v[i][j] = 1

                while stack:
                    x, y = stack.pop()
                    for k in range(8):
                        new_x, new_y = x + dx[k], y + dy[k]
                        if 0 <= new_x < h and 0 <= new_y < w:
                            if v[new_x][new_y] == 0 and lands[new_x][new_y] != 0:
                                stack.append((new_x, new_y))
                                v[new_x][new_y] = 1

    print(answer)


dx, dy = (-1, 1, 0, 0, -1, 1, -1, 1), (0, 0, -1 ,1, -1, -1, 1, 1)
while True:
    w, h = map(int, sys.stdin.readline().strip().split(" "))
    if w == 0 and h == 0:
        break

    lands = []
    for i in range(h):
        lands.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    solution()