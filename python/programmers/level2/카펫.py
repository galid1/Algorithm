def solution(brown, yellow):
    #1. y의 배치를 구한다
    #2. y의 배치를 통해 구한 b의 개수가 brown과 같은지 검사
    #3. 가로세로 길이 구하기
    y_shape = get_y_shape(brown, yellow)
    return [y_shape[0] + 2, y_shape[1] + 2]


def get_y_shape(brown, yellow):
            #  가로  , 세로
    y_shape = [yellow, 1]

    for row in range(yellow, 1, -1):
        if yellow%row == 0:
            col = yellow//row

            # 가로길이가 더 클때 까지만
            if col > row:
                break

            if brown == cal_brown_count(row, col):
                y_shape[0] = row
                y_shape[1] = col

    return y_shape


def cal_brown_count(row, col):
    return (row*2) + (col*2) + 4


# print(solution(10,2))
# print(solution(8, 1))
# print(solution(24, 24))
print(solution(16, 9))