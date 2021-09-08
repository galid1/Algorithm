import sys


def solve(a, b):
    global fir_pop, sec_pop, fir_prize, sec_prize

    fir_rank = get_rank(a, fir_pop)
    sec_rank = get_rank(b, sec_pop)

    result = fir_prize[fir_rank] + sec_prize[sec_rank]
    print(result * 10000)


def get_rank(rank, rank_pop):
    if rank == 0:
        return 0

    cur_rank = 0
    acc_pop = 0

    while rank > acc_pop:
        cur_rank += 1

        if cur_rank == len(rank_pop):
            break

        acc_pop += rank_pop[cur_rank]

    return cur_rank


t = int(sys.stdin.readline().strip())
fir_pop = [0, 1, 2, 3, 4, 5, 6]
sec_pop = [0, 1, 2, 4, 8, 16]
fir_prize = [0, 500, 300, 200, 50, 30, 10, 0]
sec_prize = [0, 512, 256, 128, 64, 32, 0]

for _ in range(t):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    solve(a, b)