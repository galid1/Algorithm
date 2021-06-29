import sys

def solution(ws):
    ws.sort(reverse=True)

    max_w = 0
    for i in range(0, len(ws)):
        max_w = max(max_w, ws[i] * (i+1))

    print(max_w)


n = int(sys.stdin.readline())
ws = []
for i in range(n):
    ws.append(int(sys.stdin.readline()))

solution(ws)