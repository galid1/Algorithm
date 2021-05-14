import sys

def solve():
    global n, l, board

    answer = 0

    # 가로 길 확인
    for i in range(n):
        idx = 0
        ch = board[i][idx]

        move_cnt = 1
        while idx < n:
            # 끝까지 이동이 가능
            if idx + 1 >= n:
                answer += 1
                break

            # 이동할 곳의 높이가 이전과 같음
            if board[i][idx+1] == ch:
                idx += 1
                move_cnt += 1
                continue

            diff = board[i][idx+1] - ch
            # 1이상 차이가 나면 이동 불가능
            if abs(diff) > 1:
                break

            # 오르막
            if diff == 1:
                if move_cnt >= l:
                    ch = board[i][idx+1]
                    move_cnt = 1
                    idx += 1
                    continue
                # 경사로 놓기 불가능
                break

            # 내리막
            if diff == -1:
                can_move = True

                # 경사로 못놓음
                if idx + l >= n:
                    break

                for j in range(idx+1, idx+l+1):
                    if board[i][j] != ch - 1:
                        can_move = False
                        break

                # 경사로 못놓음
                if not can_move:
                    break

                ch = board[i][j]
                idx = idx + l
                move_cnt = 0

    # 세로길 확인
    for i in range(n):
        idx = 0
        ch = board[idx][i]

        move_cnt = 1
        while idx < n:
            # 끝까지 이동이 가능
            if idx + 1 >= n:
                answer += 1
                break

            # 이동할 곳의 높이가 이전과 같음
            if board[idx + 1][i] == ch:
                idx += 1
                move_cnt += 1
                continue

            diff = board[idx + 1][i] - ch
            # 1이상 차이가 나면 이동 불가능
            if abs(diff) > 1:
                break

            # 오르막
            if diff == 1:
                if move_cnt >= l:
                    ch = board[idx + 1][i]
                    move_cnt = 1
                    idx += 1
                    continue
                # 경사로 놓기 불가능
                break

            # 내리막
            if diff == -1:
                can_move = True

                # 경사로 못놓음
                if idx + l >= n:
                    break

                for j in range(idx + 1, idx + l + 1):
                    if board[j][i] != ch - 1:
                        can_move = False
                        break

                # 경사로 못놓음
                if not can_move:
                    break

                ch = board[j][i]
                idx = idx + l
                move_cnt = 0


    print(answer)


n, l = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()


# 5 2
# 1 1 2 2 3
# 1 1 2 3 3
# 1 1 2 2 1
# 2 2 1 1 1
# 1 2 2 1 1