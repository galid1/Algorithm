import sys


def solve():
    global n


n = int(sys.stdin.readline().strip())
cmds = []
peoples = {}
for _ in range(n):
    people, cmd = sys.stdin.readline().strip().split(" ")
    peoples[people] = cmd


in_company = []
for people, cmd in peoples.items():
    if cmd == 'enter':
        in_company.append(people)

in_company.sort(reverse=True)
for people in in_company:
    print(people)

# 4
# Baha enter
# Askar enter
# Baha leave
# Artem enter
