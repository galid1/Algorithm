import sys
from itertools import permutations

# " 아인타는 자신이 가장 좋아하는 선수인 1번 선수를 4번 타자로 미리 결정했다."

def solve(selected_order):
    global inning, res, ans

    cur_priority = -1
    score = 0
    for cur_inning in range(inning):
        cur_priority, gain_score = play(cur_inning, cur_priority, selected_order)
        score += gain_score

    ans = max(ans, score)


# 현재 타순, 득점 반환
def play(cur_inning, cur_priority, selected_order):
    global res

    out_cnt = 0
    b1, b2, b3 = 0, 0, 0
    gain_score = 0

    # cur_priority 직전 타순이기 때문에, +1 부터 시작해야 함
    while out_cnt < 3:
        cur_priority = (cur_priority + 1) % 9
        cmd = res[cur_inning][selected_order[cur_priority]]

        if cmd == 0:
            out_cnt += 1
        elif cmd == 4:
            gain_score += b1 + b2 + b3 + 1
            b1, b2, b3 = 0, 0, 0
        elif cmd == 1:
            gain_score += b3
            b1, b2, b3 = 1, b1, b2
        elif cmd == 2:
            gain_score += b2 + b3
            b1, b2, b3 = 0, 1, b1
        elif cmd == 3:
            gain_score += b1 + b2 + b3
            b1, b2, b3 = 0, 0, 1

    return cur_priority, gain_score


# 안타: 1
# 2루타: 2
# 3루타: 3
# 홈런: 4
# 아웃: 0
inning = int(sys.stdin.readline().strip())
res = []
for _ in range(inning):
    res.append(list(map(int, sys.stdin.readline().split(" "))))

visited = [False for _ in range(9)]
visited[0] = True
ans = 0
for line_ups in permutations(range(1, 9), 8):
    line_ups = list(line_ups[:3]) + [0] + list(line_ups[3:])
    solve(line_ups)
print(ans)
