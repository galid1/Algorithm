import sys

def solution(t):
    answer = []

    answer.append(t//300)
    t %= 300

    answer.append(t//60)
    t %= 60

    answer.append(t//10)
    t %= 10

    if t != 0:
        print(-1)
    else:
        for ans in answer:
            print(ans, end= ' ')


t = int(sys.stdin.readline())
solution(t)