import sys


def solve(sx, sy, sd, fishes, eat_fish_num):
    global ds, ans

    # 물고기 이동
    move_fishes(sx, sy, fishes)

    csx, csy = sx, sy
    # 상어 이동 (먹은 물고기 배열에서 제거하기전 함수 호출 후에 제거 되어야 함)
    while True:
        nsx, nsy = csx + ds[sd][0], csy + ds[sd][1]
        will_eat_fish_idx = get_fish_idx(nsx, nsy, fishes)
        will_eat_fish_num = fishes[will_eat_fish_idx][0]
        will_eat_fish_dir = fishes[will_eat_fish_idx][1]
        # 이동 불가
        if (not fishes) or (not is_on_field(nsx, nsy)):
            ans = max(ans, eat_fish_num)
            return

        # 물고기 있음 이동 (재귀 호출하며, 먹은 물고기 증가)
        if will_eat_fish_idx != -1:
            n_fishes = fishes.copy()
            del n_fishes[will_eat_fish_idx]
            solve(nsx, nsy, will_eat_fish_dir, n_fishes, eat_fish_num + will_eat_fish_num)

        # 이동만
        csx, csy = nsx, nsy


def move_fishes(sx, sy, fishes):
    global ds

    for fi, fish in enumerate(fishes):
        cur_d = fish[1]
        cfx, cfy = fish[2]
        # 방향 전환하며 확인
        for di in range(8):
            nfx, nfy = cfx + ds[cur_d][0], cfy + ds[cur_d][1]
            # 이동 가능 (이동하고, 다음 물고기 이동)
            if is_on_field(nfx, nfy) and (nfx != sx or nfy != sy):
                will_position_fish_idx = get_fish_idx(nfx, nfy, fishes)
                # 빈칸
                if will_position_fish_idx == -1:
                    fishes[fi][2] = [nfx, nfy]
                else:
                    fishes[fi][2] = [nfx, nfy]
                    fishes[will_position_fish_idx][2] = [cfx, cfy]
                break

            cur_d = (cur_d + 1)%8


def is_on_field(x, y):
    return 0 <= x < 4 and 0 <= y < 4


def get_fish_idx(x, y, fishes):
    for idx, fish in enumerate(fishes):
        if fish[2][0] == x and fish[2][1] == y:
            return idx
    # 해당 위치에 물고기 없음
    return -1


# 위 방향부터 차례로 반시계
ds = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

fishes = []
shark_direction = 0
eat_fish_num = 0
for i in range(4):
    # 0 ~ 7
    infos = list(map(int, sys.stdin.readline().strip().split(" ")))

    for j in range(0, 8, 2):
        if i == 0 and j == 0:
            shark_direction = infos[j+1] - 1
            eat_fish_num = infos[j]
            continue
                        #번호,      방향,          위치
        fishes.append([infos[j], infos[j+1]-1, [i, j//2]])

fishes.sort(key=lambda fish: fish[0])
ans = 0
# 이미 한마리 먹고 시작
solve(0, 0, shark_direction, fishes, eat_fish_num)

print(ans)