# import sys
# 구현 방식으로 함(시간초과)
# def solve(select_cnt, selected, selected_cnt, idx):
#     global n, clothes_cnt, answer, all_kind_cnt
#
#     if selected_cnt == select_cnt:
#         res = 1
#         for cnt in selected:
#             res *= cnt
#         answer += res
#         return
#
#     for i in range(idx, all_kind_cnt):
#         selected.append(clothes_cnt[i])
#         solve(select_cnt, selected, selected_cnt+1, i+1)
#         selected.pop()
#
#
#
# t = int(sys.stdin.readline().strip())
# for _ in range(t):
#     n = int(sys.stdin.readline().strip())
#     clothes = {}
#     for _ in range(n):
#         c, t = list(sys.stdin.readline().strip().split(" "))
#         if t not in clothes.keys():
#             clothes[t] = {c}
#         else:
#             clothes[t].add(c)
#
#     clothes_cnt = []
#     for values in clothes.values():
#         clothes_cnt.append(len(values))
#
#     all_kind_cnt = len(clothes_cnt)
#     answer = 0
#     for i in range(1, all_kind_cnt+1):
#         solve(i, [], 0, 0)
#     print(answer)


# 조합론 이용(안입는 경우도 하나의 옷으로 고려하여 진행한뒤 하나도 안입는것을 뺌)
import sys

def solve():
    global clothes_cnt

    answer = 1
    for cnt in clothes_cnt:
        answer *= cnt

    print(answer - 1)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    clothes = {}
    for _ in range(n):
        c, t = list(sys.stdin.readline().strip().split(" "))
        if t not in clothes.keys():
            clothes[t] = {c}
        else:
            clothes[t].add(c)

    clothes_cnt = []
    for values in clothes.values():
        clothes_cnt.append(len(values)+1)
    solve()