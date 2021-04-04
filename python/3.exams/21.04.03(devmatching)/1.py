def solution(lottos, win_nums):
    answer = []

    right_cnt = 0
    random = 0
    for lotto in lottos:
        if lotto == 0:
            random += 1
            continue

        right, right_idx = False, 0
        for i in range(len(win_nums)):
            if lotto == win_nums[i]:
                right_cnt += 1
                right = True
                right_idx = i
                break

        if right:
            win_nums.__delitem__(right_idx)

    top = right_cnt + random
    bottom = right_cnt

    answer.append(cal_grade(top))
    answer.append(cal_grade(bottom))

    return answer


def cal_grade(count):
    if count == 6:
        return 1
    elif count == 5:
        return 2
    elif count == 4:
        return 3
    elif count == 3:
        return 4
    elif count == 2:
        return 5
    else:
        return 6

solution([44, 1, 0, 0, 31, 25]	, [31, 10, 45, 1, 6, 19]	)