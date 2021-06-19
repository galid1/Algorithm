def solution(N):
    bins = list(str(bin(N)[2:]))

    max_gap = 0

    length = 0
    for i in range(len(bins)):
        if bins[i] == '1':
            max_gap = max(max_gap, length)
            length = 0

        else:
            length += 1

    return max_gap


solution(15)