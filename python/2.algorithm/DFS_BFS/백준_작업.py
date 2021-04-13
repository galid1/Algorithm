import sys
from collections import deque

def solve():
    global cnts, times, links, n

    zeros = deque()

    # 연결 된 수가 0인것들 찾기
    for i in range(1, len(cnts)):
        if cnts[i] == 0:
            zeros.append(i)

    temp_times = [0 for i in range(n+1)]
    for zero_num in zeros:
        temp_times[zero_num] = times[zero_num]

    ans = 0
    while zeros:
        for i in range(len(zeros)):
            cur = zeros.popleft()

            #정답 갱신
            ans = max(ans, temp_times[cur])

            for link in links[cur]:
                cnts[link] -= 1
                temp_times[link] = max(temp_times[link], temp_times[cur]+times[link])

                if cnts[link] == 0:
                    zeros.append(link)
    print(ans)


n = int(sys.stdin.readline().strip())
links = {i:[] for i in range(1, n+1)}
cnts = [0 for _ in range(n+1)]
times = [0]

for i in range(1, n+1):
    inputs = list(map(int, sys.stdin.readline().strip().split(" ")))
    times.append(inputs[0])
    if inputs[1] > 0:
        for link in (inputs[2:]):
            links[link].append(i)
            cnts[i] += 1

solve()
