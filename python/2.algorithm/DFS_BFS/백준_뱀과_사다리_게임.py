import sys
from collections import deque

def solution():
    global x, y, xs, ys, ans

    q = deque()
    q.append(1)

    visit = [False for _ in range(0, 100)]
    cnt = 0
    while q:
        cnt += 1

        for i in range(len(q)):
            cur = q.popleft()

            for dice in range(1, 6+1):
                dice_res = cur + dice

                # 뱀 또는 사다리
                if dice_res in xs.keys():
                    dice_res = xs[dice_res]
                elif dice_res in ys.keys():
                    dice_res = ys[dice_res]

                if dice_res == 100:
                    ans = min(ans, cnt)
                    continue

                if dice_res < 100 and not visit[dice_res]:
                    visit[dice_res] = True
                    q.append(dice_res)


ans = sys.maxsize
x, y = map(int, sys.stdin.readline().split(" "))
xs, ys = {}, {}
for _ in range(x):
    s, e = map(int, sys.stdin.readline().strip().split(" "))
    xs[s] = e
for _ in range(y):
    s, e = map(int, sys.stdin.readline().strip().split(" "))
    ys[s] = e

solution()
print(ans)