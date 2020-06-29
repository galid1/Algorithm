import sys

# 백준 14501 퇴사

tl = [0]
pl = [0]
time = 1
res = []
n = int(sys.stdin.readline())

for i in range(n):
    t, p = map(int, sys.stdin.readline().split(" "))
    tl.append(t)
    pl.append(p)


def resignation(time = 1, profit = 0):
    if time + 1 <= n:
        resignation(time + 1, profit)
    else:
        res.append(profit)

    if time + tl[time] <= n:
        resignation(time + tl[time], profit + pl[time])
    elif time + tl[time] == n + 1:
        res.append(profit + pl[time])
    else:
        res.append(profit)

resignation()
print(max(res))
