import sys


def solve(cur_idx):
    global n, eggs, answer

    if cur_idx == n:
        answer = max(answer, get_broken_cnt())
        return

    if broken(eggs[cur_idx]):
        solve(cur_idx + 1)
        return

    attacked = False

    for target_idx in range(n):
        if target_idx == cur_idx:
            continue

        if broken(eggs[target_idx]):
            continue

        attacked = True
        attack(cur_idx, target_idx)
        solve(cur_idx+1)
        rollback_attack(cur_idx, target_idx)

    if not attacked:
        answer = max(answer, get_broken_cnt())
        return


def broken(egg):
    return egg[0] <= 0


def attack(from_idx, to_idx):
    global eggs

    eggs[from_idx][0] -= eggs[to_idx][1]
    eggs[to_idx][0] -= eggs[from_idx][1]


def rollback_attack(from_idx, to_idx):
    global eggs

    eggs[from_idx][0] += eggs[to_idx][1]
    eggs[to_idx][0] += eggs[from_idx][1]


def get_broken_cnt():
    global eggs

    result = 0
    for egg in eggs:
        if broken(egg):
            result += 1

    return result


n = int(sys.stdin.readline().strip())
eggs = []
for _ in range(n):
    eggs.append(list(map(int, sys.stdin.readline().strip().split(" "))))

answer = 0
solve(0)

print(answer)