import sys

def solve():
    global n, abils

    for i in range(1, n):
        pick_team([], i, 0)


def pick_team(cur_a_team, a_team_cnt, start_i):
    global total_team, ans
    if len(cur_a_team) == a_team_cnt:
        b_team = total_team.difference(set(cur_a_team))
        ans = min(ans, cal_abils_diff(cur_a_team, list(b_team)))
        return

    for i in range(start_i, n):
        cur_a_team.append(i)
        pick_team(cur_a_team, a_team_cnt, i+1)
        cur_a_team.pop()


def cal_abils_diff(a_team, b_team):
    return abs(cal_abil(a_team) - cal_abil(b_team))

def cal_abil(team):
    global abils

    sums = 0
    for i in range(len(team)-1):
        for j in range(i+1, len(team)):
            sums += abils[team[i]][team[j]] + abils[team[j]][team[i]]

    return sums


n = int(sys.stdin.readline().strip())
abils = []
total_team = {i for i in range(n)}
ans = sys.maxsize
for _ in range(n):
    abils.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()
print(ans)

# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0
