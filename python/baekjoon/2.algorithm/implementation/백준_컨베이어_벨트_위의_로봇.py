import sys


def solve():
    global n, k, dus, belts

    zero_dus_cnt = 0
    stage = 0
    while True:
        stage += 1
        # 벨트 이동, 로봇 내리기
        move_belts()
        # 로봇 이동
        zero_dus_cnt += move_robots()
        # 로봇 올리기
        if dus[0] >= 1:
            belts[0] = 1
            dus[0] -= 1
            if dus[0] == 0:
                zero_dus_cnt += 1
        # 내구도 검사
        if zero_dus_cnt >= k:
            break


    print(stage)


def move_belts():
    global n, belts, dus

    fir_dus, fir_belts = dus[0], belts[0]

    for i in range(2*n-1, -1, -1):
        belts[(i+1)%(2*n)] = belts[i]
        dus[(i+1)%(2*n)] = dus[i]

    belts[1], dus[1] = fir_belts, fir_dus

    # 로봇 내리기
    belts[n-1] = 0


def move_robots():
    global belts, dus, n, k

    zero_dus_cnt = 0
    for i in range(n-2, -1, -1):
        # 로봇이 존재
        if belts[i+1] == 1:
            continue

        # 내구도 1미만
        if dus[i+1] < 1:
            continue

        # 조건을 모두 만족하며 로봇이 존재하는 경우
        if belts[i] == 1:
            belts[i+1] = belts[i]
            belts[i] = 0
            dus[i+1] -= 1
            if dus[i+1] == 0:
                zero_dus_cnt += 1

        belts[n-1] = 0

    return zero_dus_cnt



n, k = map(int, sys.stdin.readline().strip().split(" "))
dus = list(map(int, sys.stdin.readline().strip().split(" ")))
belts = [0 for _ in range(len(dus))]

solve()

