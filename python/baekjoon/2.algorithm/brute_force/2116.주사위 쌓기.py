import sys


def solve():
    global n, dices

    pairs = {
        0: 5,
        1: 3,
        2: 4,
        3: 1,
        4: 2,
        5: 0
    }

    answer = 0

    # 첫번째 주사위 아래면 정하기
    for idx, phase in enumerate(dices[0]):
        bottom, top = phase, dices[0][pairs[idx]]
        cur_sums = get_max_num(bottom, top)

        for dice_idx in range(1, n):
            cur_dice = dices[dice_idx]
            cur_bottom_idx = cur_dice.index(top)
            cur_top_idx = pairs[cur_bottom_idx]
            cur_bottom, cur_top = top, cur_dice[cur_top_idx]

            cur_sums += get_max_num(cur_bottom, cur_top)
            top = cur_top

        answer = max(answer, cur_sums)

    print(answer)



def get_max_num(bottom, top):
    for num in range(6, 0, -1):
        if num != bottom and num != top:
            return num



n = int(sys.stdin.readline().strip())
dices = []
for _ in range(n):
    dices.append(list(map(int, sys.stdin.readline().strip().split(' '))))

solve()