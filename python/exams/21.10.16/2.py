from itertools import combinations

def solution(leave, day, holidays):
    calendar = [False for _ in range(31)]

    mark_weekend(calendar, day)
    mark_holidays(calendar, holidays)

    all_days = set(i for i in range(1, 31))
    tmp_calendar = [False for _ in range(31)]

    answer = -100
    for leaves in combinations(all_days, leave):
        mark_leaves(tmp_calendar, leaves)
        leave_day = cal_leave_day(calendar, tmp_calendar, answer)
        unmark_leaves(tmp_calendar, leaves)

        answer = max(answer, leave_day)

    return answer


def mark_leaves(calendar, leaves):
    for leave in leaves:
        calendar[leave] = True

def unmark_leaves(calendar, leaves):
    for leave in leaves:
        calendar[leave] = False


def cal_leave_day(calendar, tmp_calendar, answer):
    max_leave_day = 0
    for start in range(1, 31):
        if answer >= 30 - start + 1:
            break

        # 시작날이 쉬는날도 아니고 휴가도 아니면 다음으로
        if not calendar[start] and not tmp_calendar[start]:
            continue

        cur_leave_day = 1
        i = start + 1
        while i <= 30 and (calendar[i] or tmp_calendar[i]):
            cur_leave_day += 1
            i += 1

        max_leave_day = max(max_leave_day, cur_leave_day)

    return max_leave_day



def mark_weekend(calendar, day):
    closest_sat_diff = 0

    if day == "MON":
        closest_sat_diff = 5
    elif day == "TUE":
        closest_sat_diff = 4
    elif day == "WED":
        closest_sat_diff = 3
    elif day == "THU":
        closest_sat_diff = 2
    elif day == "FRI":
        closest_sat_diff = 1
    elif day == "SAT":
        closest_sat_diff = 0
        calendar[1] = True
        calendar[2] = True
    elif day == "SUN":
        closest_sat_diff = 6
        calendar[1] = True

    idx = 1 + closest_sat_diff

    calendar[idx] = True
    calendar[idx+1] = True

    A_WEEK = 7
    while idx + A_WEEK <= 30:
        idx += A_WEEK

        calendar[idx] = True

        if idx+1 > 30:
            break

        calendar[idx+1] = True


def mark_holidays(calendar, holidays):
    for holiday in holidays:
        calendar[holiday] = True


# leave = 4
# day = "FRI"
# holidays = [6, 21, 23, 27, 28]

# leave = 3
# day = "SUN"
# holidays = [2, 6, 17, 29]


leave = 30
day = "MON"
holidays = [1, 2, 3, 4, 28, 29, 30]
print(solution(leave, day, holidays))
