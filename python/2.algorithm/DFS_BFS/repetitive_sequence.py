# 백준 2331번 반복수열

import sys

def solve(a, p):
    visit[a] = 1

    next = a
    while True:
        next = get_next(next, p)

        if visit[next] > 3:
            return

        visit[next] += 1


def get_next(a, p):
    result = 0

    while a:
        result += pow(a % 10, p)
        a = a // 10

    return result


visit = [0 for i in range(300000)]
a, p = map(int, sys.stdin.readline().split(" "))
solve(a, p)
answer = 0
for num in visit:
    if num == 1:
        answer += 1
print(answer)