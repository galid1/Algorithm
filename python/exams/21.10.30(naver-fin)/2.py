def solution(n, jump):
    answer = []
    # 방향 정보
    ds = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    R, D, L, U = 0, 1, 2, 3

    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[0][0] = 1

    dir = U
    cur_num, end_num = 0, n*n
    remain_jump = jump
    hor_move, ver_move = n, n
    cur_num = 1
    cx, cy = 0, -1
    while True:
        dir = get_next(dir)
        dx, dy = ds[dir]

        move_num = hor_move if dir == L or dir == R else ver_move
        for _ in range(move_num):
            cx, cy = cx+dx, cy+dy

            if board[cx][cy] == -1:
                remain_jump -= 1

            if remain_jump == 0:
                cur_num += 1
                board[cx][cy] = cur_num
                remain_jump = jump

            if cur_num == end_num:
                return [cx+1, cy+1]

        if dir == L or dir == R:
            ver_move -= 1
        else:
            hor_move -= 1

        if hor_move == 0 or ver_move == 0:
            cx, cy = 0, -1
            hor_move, ver_move = n, n
            dir = U

    return answer


def get_next(cur_dir):
    return (cur_dir+1) % 4


n = 3
jump = 10
print(solution(n, jump))