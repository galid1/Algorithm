import sys

def solution(k, cur):
    tk = k
    answer = 0

    for i in range(len(cur) - 1, -1, -1):
        if k // cur[i] == 0:
            continue

        answer += tk // cur[i]
        tk = tk % cur[i]

        if tk == 0:
            print(answer)
            return


n, k = map(int, sys.stdin.readline().split(" "))
cur = []
for i in range(n):
    cur.append(int(sys.stdin.readline()))
solution(k, cur)
