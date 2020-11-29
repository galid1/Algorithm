import sys


def solution():
    global target_channel, brokens
    non_brokens = {i for i in range(10)}.difference(brokens)
    start_channel = 100

    answer = abs(start_channel - target_channel)

    for channel in range(1000000):
        if set(map(int, str(channel))).issubset(non_brokens):
            count = len(str(channel)) + abs(channel - target_channel)
            answer = min(answer, count)

    print(answer)


target_channel = int(sys.stdin.readline())
broken_count = int(sys.stdin.readline())
if broken_count > 0:
    brokens = set(map(int, sys.stdin.readline().strip().split(" ")))
else:
    brokens = set()
solution()