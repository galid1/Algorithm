import sys


def solve():
    global n, k, infos

    ranks = {infos[0][0]: 1}
    infos.sort(key=lambda item: (item[1], item[2], item[3]), reverse=True)

    rank = 1
    tie_cnt = 1
    for idx in range(1, n):
        if is_tie(idx-1, idx):
            tie_cnt += 1
        else:
            adder = 1
            if tie_cnt > 1:
                adder = tie_cnt
            rank += adder

        ranks[infos[idx][0]] = rank

    print(ranks[k])


def is_tie(a_idx, b_idx):
    global infos
    return infos[a_idx][1:] == infos[b_idx][1:]


n, k = map(int, sys.stdin.readline().strip().split(" "))
infos = []
for _ in range(n):
    infos.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()

# 4 3
# 1 1 2 0
# 2 1 3 0
# 3 1 1 0
# 4 1 2 1