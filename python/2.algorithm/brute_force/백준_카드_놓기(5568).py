import sys


def solve(cur, cnt, start_i):
    global n, k, cards, ans, selected_cards

    if cnt == k:
        selected_cards.append(cur.copy())
        return

    for i in range(start_i, n):
        cur.append(cards[i])
        solve(cur, cnt+1, i+1)
        cur.pop()


def get_kind_of_cnt():
    global selected_cards

    made_nums = set()
    for cards in selected_cards:
        visited = [False for _ in range(4)]
        make_num("", 0, cards, made_nums, visited)
    return made_nums


def make_num(cur, cnt, cards, made_nums, visited):
    global k

    if cnt == k:
        made_nums.add(cur)
        return


    for idx, card in enumerate(cards):
        if visited[idx]:
            continue

        visited[idx] = True
        make_num(cur+str(card), cnt+1, cards, made_nums, visited)
        visited[idx] = False


n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
cards = []

for _ in range(n):
    cards.append(int(sys.stdin.readline().strip()))

selected_cards = []
ans = 0
solve([], 0, 0)
print(len(get_kind_of_cnt()))
