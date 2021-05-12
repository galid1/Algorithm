import sys


def solve(n, direction, bef):
    global ss, ms, k

    next_direction = get_next_direction(direction)

    # 첫 바퀴
    if n == 1:
        # 이전이 2번째 바퀴면 그만
        if bef != 2:
            if can_spin(ss[1], ss[2]):
                solve(2, next_direction, 1)

    # 두번째 바퀴
    elif n == 2:
        if bef != 1:
            if can_spin(ss[1], ss[2]):
                solve(1, next_direction, 2)
        if bef != 3:
            if can_spin(ss[2], ss[3]):
                solve(3, next_direction, 2)

    elif n == 3:
        if bef != 2:
            if can_spin(ss[2], ss[3]):
                solve(2, next_direction, 3)
        if bef != 4:
            if can_spin(ss[3], ss[4]):
                solve(4, next_direction, 3)

    elif n == 4:
        if bef != 3:
            if can_spin(ss[3], ss[4]):
                solve(3, next_direction, 4)

    spin(n, direction)



def get_next_direction(direction):
    return -1 if direction == 1 else 1


# s1이 왼쪽에 위치한 톱니, s2는 오른쪽
def can_spin(s1, s2):
    if s1[2] != s2[6]:
        return True
    return False


def spin(n, direction):
    global ss

    # 시계 방향
    if direction == 1:
        # print(" 정방향 회전 ----- ")
        # print(ss[n])
        t = ss[n][7]
        for i in range(6, -1, -1):
            ss[n][i+1] = ss[n][i]
        ss[n][0] = t
        # print(ss[n])
    # 반시계 방향
    else:
        t = ss[n][0]
        for i in range(7):
            ss[n][i] = ss[n][i + 1]
        ss[n][7] = t


ss = [[]]
for _ in range(4):
    ss.append(list(sys.stdin.readline().strip()))
k = int(sys.stdin.readline().strip())
for _ in range(k):
    n, d = map(int, sys.stdin.readline().strip().split(" "))
    solve(n, d, 0)

# 답
ans = 0
if ss[1][0] == '1':
    ans += 1
if ss[2][0] == '1':
    ans += 2
if ss[3][0] == '1':
    ans += 4
if ss[4][0] == '1':
    ans += 8
print(ans)