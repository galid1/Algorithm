import sys

v = [False for _ in range(31)]

for _ in range(28):
    num = int(sys.stdin.readline().strip())
    v[num] = True


not_submits = []
for i in range(1, 31):
    if not v[i]:
        not_submits.append(i)

not_submits.sort()

for not_submit in not_submits:
    print(not_submit)