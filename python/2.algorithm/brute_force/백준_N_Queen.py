# 파이썬을 이용하면 시간초과가 날수 밖에 없다고는 함 ...
import sys

def solution(row_idx):
    global visit, answer

    if row_idx == len(visit):
        answer += 1
        return

    print("============ row idx : ", row_idx)
    for col_idx in range(len(visit[0])):
        if is_valid(row_idx, col_idx):
            visit[row_idx][col_idx] = 1
            solution(row_idx + 1)
            visit[row_idx][col_idx] = 0


def is_valid(row, col):
    # 왼쪽 위 대각선 라인 검사 (row마다 1씩 뺌)
    diagonal_l_col = col
    # 오른쪽 위 대각선 라인 검사 (row마다 1씩 더함)
    diagonal_r_col = col

    # 방금 놓은 체스말의 윗 라인부터 검사시작
    for i_row in range(row - 1, -1, -1):
        # 같은 라인 검사
        if visit[i_row][col]:
            return False

        # 왼쪽 대각선 검사
        if diagonal_l_col - 1 >= 0 and visit[i_row][diagonal_l_col - 1]:
            return False

        # 오른쪽 대각선 검사
        if diagonal_r_col + 1 < len(visit[0]) and visit[i_row][diagonal_r_col + 1]:
            return False

        diagonal_l_col -= 1
        diagonal_r_col += 1

    return True


n = int(sys.stdin.readline())
answer = 0
visit = [[0 for i in range(n)] for j in range(n)]
solution(0)
print(answer)