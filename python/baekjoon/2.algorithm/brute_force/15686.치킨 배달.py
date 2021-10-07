import sys
from itertools import combinations
from collections import deque


def solve():
    global board, m

    hs, cs = find_positions()

    ans = sys.maxsize
    for selected in combinations(cs, m):
        result = get_chicken_distance(selected, hs)
        ans = min(ans, result)

    print(ans)


def get_chicken_distance(selected, hs):
    global board, n

    city_chicken_distance = 0

    for hx, hy in hs:
        min_chicken_distance = 30000
        for cx, cy in selected:
            min_chicken_distance = min(min_chicken_distance, abs(hx-cx) + abs(hy-cy))
        city_chicken_distance += min_chicken_distance

    return city_chicken_distance


def valid(x, y):
    global n

    return 0 <= x < n and 0 <= y < n


def find_positions():
    global board, n

    houses, chickens = set(), set()

    for i in range(n):
        for j in range(n):
            if board[i][j] == "1":
                houses.add((i, j))
            elif board[i][j] == "2":
                chickens.add((i, j))

    houses =  sorted(houses, key=lambda item: (item[0], item[1]))
    chickens = sorted(chickens, key=lambda item: (item[0], item[1]))
    return houses, chickens


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip().split(" ")))

solve()