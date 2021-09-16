import sys
from collections import defaultdict


def solve():
    global n, dots

    dot_map = defaultdict(list)

    # group 화
    for position, color in dots:
        dot_map[color].append(position)

    # 정렬
    for color in dot_map.keys():
         dot_map[color].sort()

    answer = 0
    for dots in dot_map.values():
        if len(dots) <= 1:
            continue

        for idx in range(len(dots)):
            if idx == 0:
                answer += abs(dots[idx] - dots[idx+1])

            elif idx < len(dots)-1:
                answer += min(abs(dots[idx-1] - dots[idx]), abs(dots[idx] - dots[idx+1]))

            else:
                answer += abs(dots[idx] - dots[idx-1])

    print(answer)



n = int(sys.stdin.readline().strip())
dots = []
for _ in range(n):
    dots.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()