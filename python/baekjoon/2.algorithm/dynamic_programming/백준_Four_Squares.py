import sys


def solve():
    global n

    d = [0 for _ in range(n+1)]

    for num in range(1, n+1):
        reverse_square_nbm = int(pow(num, 0.5))
        if pow(reverse_square_nbm, 2) == num:
            d[num] = 1
            continue

        else:
            min_cnt = 10000
            square_num_i = 1
            while True:
                cur_square_num = pow(square_num_i, 2)

                if cur_square_num > num:
                    break

                min_cnt = min(min_cnt, 1 + d[num - cur_square_num])
                square_num_i += 1

            d[num] = min_cnt

    print(d[n])


n = int(sys.stdin.readline().strip())
solve()

