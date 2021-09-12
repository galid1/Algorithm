from itertools import combinations_with_replacement
from collections import Counter


def solution(n, info):
    apc_cnt = get_cnt(info)

    # 가장 큰 점수차 결과 모으기 위한 변수
    max_diff_grade = -1
    lion_cnts = []

    for lion_info in list(combinations_with_replacement([i for i in range(10, -1, -1)], n)):
        lion_cnt = get_lion_cnt(Counter(lion_info))

        grade_diff = cal_grade_diff(apc_cnt, lion_cnt)
        if grade_diff > max_diff_grade:
            max_diff_grade = grade_diff
            lion_cnts = [lion_cnt]
        elif grade_diff == max_diff_grade:
            lion_cnts.append(lion_cnt)

    if max_diff_grade <= 0:
        return [-1]


    return get_answer(lion_cnts)


def cal_grade_diff(apc_cnt, lion_cnt):
    result = 0

    for grade in range(11):
        if apc_cnt[grade] == 0 and lion_cnt[grade] == 0:
            continue

        if apc_cnt[grade] >= lion_cnt[grade]:
            result -= grade
        else:
            result += grade

    return result


def get_cnt(info):
    grade_cnt = {}

    for idx, cnt in enumerate(info):
        grade_cnt[10-idx] = cnt

    return grade_cnt


def get_lion_cnt(info):
    grade_cnt = {i: 0 for i in range(10, -1, -1)}

    for grade, cnt in info.items():
        grade_cnt[grade] = cnt

    return grade_cnt


def get_answer(lion_cnts):
    for grade in range(11):
        max_cnt = 0
        li = []

        for cnt in lion_cnts:
            if cnt[grade] > max_cnt:
                max_cnt = cnt[grade]
                li = [cnt]
            elif cnt[grade] == max_cnt:
                li.append(cnt)

        lion_cnts = li

    return list(lion_cnts[0].values())



# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]

# n = 1
# info = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# n = 9
# info = [0,0,1,2,0,1,1,1,1,1,1]

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))


