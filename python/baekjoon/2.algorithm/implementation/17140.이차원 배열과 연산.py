import sys
from collections import defaultdict


def solve(r, c, k, a):
    r_cnt, c_cnt = 3, 3

    for ans in range(101):
        if is_end(r, c, k, a):
            return print(ans)

        r_cnt, c_cnt, a = r_or_c(r_cnt, c_cnt, a)

    # 정답이 나오지 않음
    print(-1)


def r_or_c(r_cnt, c_cnt, a):
    def do_r(a):
        new_a = []
        max_row_length = 0

        for row in a:
            cnts = defaultdict(int)

            for num in row:
                if num == 0:
                    continue
                cnts[num] += 1

            # 정렬
            cnts = sort_dict(cnts)
            new_row = flatten(cnts)
            new_a.append(new_row)

            # 제일 긴 행 갱신
            max_row_length = max(max_row_length, len(new_row))

        # 크기가 모자른 행은 0을 모자른 크기만큼 추가
        for idx, row in enumerate(new_a):
            need_cnt = max_row_length - len(row)
            new_a[idx] += [0] * need_cnt

        return new_a, max_row_length

    def do_c(a):
        max_col_length = len(a)
        new_a = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]

        for col in range(len(a[0])):
            cnts = defaultdict(int)
            for row in range(len(a)):
                num = a[row][col]
                if num == 0:
                    continue
                cnts[num] += 1

            # 정렬
            cnts = sort_dict(cnts)
            new_col = flatten(cnts)

            # 부족한 길이가 있다면 0배열 추가
            need_row_cnt = len(new_col) - max_col_length
            for _ in range(need_row_cnt):
                new_a.append([0 for _ in range(cur_c_cnt)])

            # 제일 긴 col 갱신
            max_col_length = max(max_col_length, len(new_col))
            for row in range(len(new_col)):
                new_a[row][col] = new_col[row]

        return new_a, max_col_length


    cur_r_cnt, cur_c_cnt = r_cnt, c_cnt

    if cur_r_cnt >= cur_c_cnt:
        a, cur_c_cnt = do_r(a)
    else:
        a, cur_r_cnt = do_c(a)

    return cur_r_cnt, cur_c_cnt, a


def sort_dict(cnts):
    cnts = dict(sorted(cnts.items(), key=lambda item: item[0]))
    return dict(sorted(cnts.items(), key=lambda item: item[1]))


def flatten(cnts):
    new_row = []
    for items in cnts.items():
        for item in items:
            new_row.append(item)

    return new_row


def is_end(r, c, k, a):
    if r > len(a)-1 or c > len(a[0]) - 1:
        return False

    return a[r][c] == k


r, c, k = map(int, sys.stdin.readline().strip().split(" "))
r, c = r - 1, c - 1

a = []
for _ in range(3):
    a.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve(r, c, k, a)