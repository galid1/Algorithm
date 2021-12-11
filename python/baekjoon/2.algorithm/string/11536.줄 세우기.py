import sys


def solve():
    global n, ss, EQUAL, INCREASING, DECREASING

    bef_order = "NEITHER"
    for idx in range(1, n):
        cur_order = get_order(ss[idx-1], ss[idx])

        if bef_order == "NEITHER":
            bef_order = cur_order
            continue

        if cur_order == EQUAL:
            continue

        elif cur_order != bef_order:
            return print("NEITHER")

    print(bef_order)


def get_order(bef, cur):
    global EQUAL, INCREASING, DECREASING

    if bef > cur:
        return DECREASING
    elif bef < cur:
        return INCREASING
    else:
        return EQUAL


EQUAL = 'NEITHER'
INCREASING = 'INCREASING'
DECREASING = 'DECREASING'
n = int(sys.stdin.readline().strip())
ss = []
for _ in range(n):
    ss.append(sys.stdin.readline().strip())

solve()


# 2번째 부터 시작.
# 이전과 비교해서 큰지 작은지 같은지 비교
# 비교 결과 문자 받아오기
# 이전 문자가 비어있거나 equal면 이전문자에 적용후 다음으로
# 결과가 equal이면 continue
# 이전문자와 다르다면 NEITHER 출력 후 반환
# 결과 출력

