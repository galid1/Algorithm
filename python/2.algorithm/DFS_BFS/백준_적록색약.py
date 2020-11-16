import sys


def solution():
    print(dfs(normal_cond), end=' ')
    print(dfs(un_normal_cond))


def dfs(cond):
    v = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0
    s = []
    for i in range(n):
        for j in range(n):
            if not v[i][j]:
                answer += 1
                s.append((i, j))
                color = picture[i][j]
                while s:
                    x, y = s.pop()

                    for k in range(4):
                        new_x = x + dx[k]
                        new_y = y + dy[k]

                        if is_in_picture(new_x, new_y) and not v[new_x][new_y] and cond(color, picture[new_x][new_y]):
                                v[new_x][new_y] = 1
                                s.append((new_x, new_y))

    return answer


def is_in_picture(x, y):
    return True if 0 <= x < n and 0 <= y < n else False


def normal_cond(origin_color, target_color):
    return True if origin_color == target_color else False


def un_normal_cond(origin_color, target_color):
    if origin_color == 'R' or origin_color == 'G':
        if target_color == 'R' or target_color == 'G':
            return True
        else:
            False
    else:
        return True if target_color == 'B' else False


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
n = int(sys.stdin.readline())
picture = []
for i in range(n):
    picture.append(list(sys.stdin.readline().strip()))
solution()