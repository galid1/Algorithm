from itertools import combinations
from collections import defaultdict

def solution(orders, course):
                    #    comb  cnt
    answer = {course_cnt: [['', 0]] for course_cnt in course}

    order_combs = defaultdict(int)

    for order_line in orders:
        list_order_line = list(order_line)
        list_order_line.sort()

        for course_cnt in course:
            for comb in list(combinations(list_order_line, course_cnt)):
                order_combs[comb] += 1

    for comb, order_cnt in order_combs.items():
        if order_cnt < 2:
            continue

        course_cnt = len(comb)
        comb = ''.join(comb)
        if answer[course_cnt][0][1] < order_cnt:
            answer[course_cnt] = [[comb, order_cnt]]
        elif answer[course_cnt][0][1] == order_cnt:
            answer[course_cnt].append([comb, order_cnt])

    res = []
    for menus in answer.values():
        if not menus[0][0]:
            continue

        for menu in menus:
            res.append(menu[0])

    res.sort()

    return res


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))
