import sys

def solution(target_sums):
    i = 1
    while i * (i + 1) // 2 <= target_sums:
        i += 1

    print(i - 1)


s = int(sys.stdin.readline())
solution(s)