import sys


def solution():
    global n, l, positions

    answer = 0
    positions.sort()

    standard_idx = 0
    while standard_idx < len(positions):
        answer += 1

        standard = positions[standard_idx]
        compare_idx = standard_idx + 1

        can_contain_remains = True
        while compare_idx < len(positions):
            if abs(positions[compare_idx] - standard) + 1 > l:
                standard_idx = compare_idx
                can_contain_remains = False
                break
            else:
                compare_idx += 1

        if can_contain_remains:
            break

    print(answer)


n, l = map(int, sys.stdin.readline().strip().split(" "))
positions = list(map(int, sys.stdin.readline().strip().split(" ")))
solution()
