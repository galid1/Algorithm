import sys


def solution():
    global coins
    targets = 0, 1
    answers = []
    for j in range(2):
        target = targets[j]

        bef = -1
        answer = 0
        for i in range(len(coins)):
            if target != coins[i] and bef != coins[i]:
                answer += 1
            bef = coins[i]

        answers.append(answer)

    # 정답
    print(min(answers))

coins = list(map(int, sys.stdin.readline().strip()))
solution()
