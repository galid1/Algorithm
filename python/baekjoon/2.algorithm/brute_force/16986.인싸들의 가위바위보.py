import sys
from collections import deque


def play(game_idx, play_now, target):
    global play_table, target_actions, scores, n, visited

    if is_end(game_idx):
        return

    if play_now:
        for action_idx in range(n):
            if visited[action_idx]:
                continue

            visited[action_idx] = True
            target_act = target_actions[target].popleft()
            result = rsp(action_idx, target_act)

            if result == 2:
                scores[0] += 1
                play(game_idx + 1, play_now, get_next_target(target))
                scores[0] -= 1
            else:
                scores[target] += 1
                play(game_idx + 1, not play_now, target)
                scores[target] -= 1

            visited[action_idx] = False
            target_actions[target].appendleft(target_act)

    else:
        other = get_next_target(target)

        p1_act = target_actions[target].popleft()
        p2_act = target_actions[other].popleft()
        result = rsp(p1_act, p2_act)

        if result == 2:
            scores[target] += 1
            play(game_idx + 1, not play_now, target)
            scores[target] -= 1
        elif result == 1:
            if target > other:
                scores[target] += 1
                play(game_idx + 1, not play_now, target)
                scores[target] -= 1
            else:
                scores[other] += 1
                play(game_idx + 1, not play_now, other)
                scores[other] -= 1
        else:
            scores[other] += 1
            play(game_idx + 1, not play_now, other)
            scores[other] -= 1

        target_actions[target].appendleft(p1_act)
        target_actions[other].appendleft(p2_act)


def rsp(p1_act, p2_act):
    global play_table

    return play_table[p1_act][p2_act]



def get_next_target(target):
    return 1 if target == 2 else 2


def is_end(game_idx):
    global scores, k, ans

    if game_idx >= 20:
        return True

    if ans == 1:
        return True

    for idx, score in enumerate(scores):
        if score >= k:
            if idx == 0:
                ans = 1
            return True

    return False


n, k = map(int, sys.stdin.readline().strip().split(' '))
play_table = []
for _ in range(n):
    play_table.append(list(map(int, sys.stdin.readline().strip().split(" "))))

target_actions = [[]]
target_actions.append(deque(map(lambda item: int(item) - 1, sys.stdin.readline().strip().split(' '))))
target_actions.append(deque(map(lambda item: int(item) - 1, sys.stdin.readline().strip().split(' '))))

scores = [0, 0, 0]
visited = [False for _ in range(n)]
ans = 0
play(0, True, 1)

print(ans)