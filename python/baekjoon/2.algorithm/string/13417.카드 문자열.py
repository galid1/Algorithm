import sys
from collections import deque


def solve():
    global n, cards

    ans = deque()
    for card in cards:
        if not ans:
            ans.append(card)
            continue

        if card > ans[0]:
            ans.append(card)
        elif card == ans[0]:
            if card <= ans[-1]:
                ans.appendleft(card)
            else:
                ans.append(card)
        else:
            ans.appendleft(card)

    print(''.join(ans))



t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    cards = list(sys.stdin.readline().strip().split(" "))
    solve()