import sys


def solve():
    global n, infos

    infos.sort(key=lambda items: items[0])
    infos.sort(key=lambda items: items[3], reverse=True)
    infos.sort(key=lambda items: items[2])
    infos.sort(key=lambda items: items[1], reverse=True)

    for info in infos:
        print(info[0])


n = int(sys.stdin.readline().strip())
infos = []
for _ in range(n):
    info = sys.stdin.readline().strip().split(" ")
    infos.append(tuple(map(lambda item: int(item) if item.isnumeric() else item, info)))

solve()
