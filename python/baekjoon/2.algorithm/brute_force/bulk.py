# baekjoon 7568 덩치

import sys

def solve(bluks):
    rank_list = []

    for i in range(len(bulks)):
        i_rank = get_rank(i, bulks)
        rank_list.append(i_rank)

    print_rank_list(rank_list)


def get_rank(cur_index, bulks):
    cur_bulks = bulks[cur_index]

    rank = 1
    for i in range(len(bulks)):
        if i == cur_index:
            continue

        if is_smaller_than(cur_bulks, bulks[i]):
            rank += 1

    return rank


# comparison_bulks보다 더 작으면 True 반환
def is_smaller_than(cur_bulks, comparison_bulk):
    if cur_bulks[0] < comparison_bulk[0] and cur_bulks[1] < comparison_bulk[1]:
        return True

    return False


def print_rank_list(rank_list):
    for rank in rank_list:
        print(rank, end=' ')


n = int(sys.stdin.readline())
bulks = []

for i in range(n):
    bulks.append(list(map(int, sys.stdin.readline().split(" "))))


solve(bulks)
