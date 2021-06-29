# 오른쪽 : 1  === 4 1 2 3
# 아래 : 2 === 1 2 3 4
# 왼쪽 : 3 === 2 3 4 1
# 위 : 4 === 3 4 1 2


def solution(maze):
    answer = 0
    #     X  1  2  3  4 (방향)
    dx = [0, 1, 0, -1, 0]
    dy = [0, 0, 1, 0, -1]

    # 최초 진행방향 아래
    direction = 2
    # 최초 시작 [0, 0]
    cur = [0, 0]

    while True:
        # 다음 진행
        next = direction - 2

        while True:
            # 목적지
            if cur[0] == len(maze) - 1 and cur[1] == len(maze) - 1:
                return answer

            # 이번에 시도할 움직임
            move = next % 4 + 1
            # 다음 준비
            next = next + 1

            # 이동가능 파악 후 이동
            move_x = cur[0] + dx[move]
            move_y = cur[1] + dy[move]
            if 0 <= move_x < len(maze):
                cur[0] = cur[0] + dx[move]
                answer += 1

            if 0 <= move_y < len(maze):
                cur[1] = cur[1] + dx[move]
                answer += 1

    return answer


def move_next(maze, dx, dy, cur, direction):
    next = direction - 2
    count = 0

    while True:
        # 이번에 시도할 움직임
        move = next % 4 + 1
        # 다음 준비
        next = next + 1
        # 4방향 시도를 위한 카운트
        count += 1

        if count == 4:
            break


print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))