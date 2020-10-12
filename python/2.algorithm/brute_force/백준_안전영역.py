import sys, copy


def solution(area):
    max_h = max(map(max, area))

    answers = []

    for rain_h in range(max_h-1, -1, -1):
        t_area = copy.deepcopy(area)
        rain(t_area, rain_h)

        cnt = 0
        for i in range(len(t_area)):
            for j in range(len(t_area[0])):
                if t_area[i][j] != 0:
                    cnt += 1
                    dfs(t_area, i, j)

        answers.append(cnt)

    print(max(answers))


def rain(area, rain_h):
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j] <= rain_h:
                area[i][j] = 0


def dfs(area, row, col):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [row, col]
    area[row][col] = 0

    while stack:
        cur_col = stack.pop()
        cur_row = stack.pop()

        for i in range(4):
            n_row = cur_row + dx[i]
            n_col = cur_col + dy[i]

            if 0 <= n_row < len(area) and 0 <= n_col < len(area[0]) and area[n_row][n_col]:
                stack.append(n_row)
                stack.append(n_col)
                area[n_row][n_col] = 0




n = int(sys.stdin.readline())
area = []
for i in range(n):
    area.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solution(area)

