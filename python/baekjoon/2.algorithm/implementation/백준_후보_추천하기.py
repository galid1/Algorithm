import sys


def solve():
    global size, n, votes

    cur_size = 0
    casts = []

    for idx, vote in enumerate(votes):
        is_in_casts, real_idx = is_in(casts, vote)

        if is_in_casts:
            casts[real_idx][2] += 1
        else:
            if is_full(cur_size):
                casts.pop()
                cur_size -= 1
            casts.append([idx, vote, 1])
            cur_size += 1

        casts.sort(key=lambda item: item[0], reverse=True)
        casts.sort(key=lambda item: item[2], reverse=True)

    casts.sort(key=lambda item: item[1])
    for idx, candidate, vote_num in casts:
        print(candidate, end=' ')


def is_full(cur_size):
    global size

    if cur_size >= size:
        return True
    return False


def is_in(casts, vote):
    real_idx = -1

    for idx, candidate, vote_num in casts:
        real_idx += 1
        if candidate == vote:
            return True, real_idx
    return False, 0

size = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
votes = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()
