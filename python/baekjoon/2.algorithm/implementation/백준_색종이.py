# import sys
#
#
# def solve():
#     global n, coords
#
#     # 종이의 개수 * 100에서 겹차는 부분을 차감하는 방식
#     answer = 10*10*n
#
#     for i in range(n):
#         for j in range(i+1, n):
#             if is_overlap(i, j):
#                 print("overlap : ", i ,j)
#                 oa = cal_overlap_area(i, j)
#                 print(oa)
#                 answer -= oa
#
#     print(answer)
#
#
# def is_overlap(i, j):
#     global coords
#
#     x1, y1 = coords[i]
#     x2, y2 = coords[j]
#
#     if x1 > x2:
#         x1, x2 = x2, x1
#     if y1 > y2:
#         y1, y2 = y2, y1
#
#     if x1 + 10 > x2 and y1 + 10 > y2:
#         return True
#     return False
#
#
# def cal_overlap_area(i, j):
#     global coords
#
#     x1, y1 = coords[i]
#     x2, y2 = coords[j]
#
#     return (10 - abs(x1 - x2)) * (10 - abs(y1 - y2))
#
#
# n = int(sys.stdin.readline().strip())
# coords = []
# for _ in range(n):
#     y, x = map(int, sys.stdin.readline().strip().split(" "))
#     coords.append((x, y))
#
# solve()
#
# # 3
# # 1 3
# # 2 4
# # 3 1

import sys


def solve():
    global n, coords

    board = [[False for _ in range(101)] for _ in range(101)]

    for x, y in coords:
        for i in range(x, x+10):
            for j in range(y, y+10):
                board[i][j] = True

    answer = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if board[i][j]:
                answer += 1

    print(answer)


n = int(sys.stdin.readline().strip())
coords = []
for _ in range(n):
    y, x = map(int, sys.stdin.readline().strip().split(" "))
    coords.append((x, y))

solve()