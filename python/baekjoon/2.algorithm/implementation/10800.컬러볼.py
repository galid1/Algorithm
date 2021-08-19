import sys
from collections import defaultdict


# def solve(infos):
#     acc_colors = defaultdict(int)
#     sums = 0
#
#     append_idx(infos)
#     infos = sort_by_color_and_size(infos)
#
#     total_sum = 0
#     # color별 누적
#     color_acc = defaultdict(int)
#
#     # 같은 크기 누적
#     cur_size = -1
#     cur_same_size_sum = 0
#     same_color_size = defaultdict(int)
#
#     # ans 구하기
#     ans = defaultdict(int)
#     for color, size, idx in infos:
#         # 현재 같은 크기 정보 갱신
#         if size != cur_size:
#             cur_size = size
#             same_color_size = defaultdict(int)
#             same_color_size[color] += size
#             cur_same_size_sum = size
#         else:
#             same_color_size[color] += size
#             cur_same_size_sum += size
#
#         ans[idx] = total_sum - color_acc[color] - (cur_same_size_sum - same_color_size[color])
#
#         # 누적
#         total_sum += size
#         color_acc[color] += size
#
#
#     ans = sorted(ans.items(), key=lambda item:item[0])
#     # 임시 출력
#     for an in ans:
#         print(an[1])


# 2 포인터 풀이
def solve(infos):
    append_idx(infos)
    infos = sort_by_color_and_size(infos)

    ans = defaultdict(int)
    acc = 0
    color_acc = defaultdict(int)
    j = 0
    for i in range(len(infos)):
        cur_color, cur_size, idx = infos[i]

        compared_color, compared_size, compared_idx = infos[j]

        while cur_size > compared_size:
            acc += compared_size
            color_acc[compared_color] += compared_size
            j += 1
            compared_color, compared_size, compared_idx = infos[j]

        ans[idx] = acc - color_acc[cur_color]

    ans = sorted(ans.items(), key=lambda item:item[0])
    for an in ans:
        print(an[1])


def append_idx(infos):
    for idx, info in enumerate(infos):
        info.append(idx)


def sort_by_color_and_size(infos):
    infos = sorted(infos, key=lambda item: item[0])
    infos = sorted(infos, key=lambda item: item[1])
    return infos


n = int(sys.stdin.readline().strip())
infos = []
for _ in range(n):
    infos.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve(infos)

# 8
# 1 10
# 2 15
# 1 3
# 4 20
# 2 1
# 1 5
# 4 7
# 3 3

# 8
# 2 2
# 2 2
# 2 2
# 3 3
# 1 5
# 1 1
# 1 1
# 1 1

# 8
# 2 2
# 2 2
# 2 2
# 3 2
# 1 2
# 1 1
# 1 1
# 1 1
