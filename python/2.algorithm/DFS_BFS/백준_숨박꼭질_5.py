import sys
from collections import deque

# 언니는, 왔다 갔다 하며 재자리로 돌아올 수가 있다. (n+1, n-1)
# 이때, 해당 수를 계속해서 재방문 하는 것은, 시간초과가 된다.
# 하지만, 그렇다고 왔다 갔다 하는 것을, 못하게 만들면 왔다 갔다 하는 것으로 만날 경우를 배제하는 꼴이 된다.
# 따라서, 홀수 짝수 방문 배열을 만들고, 한번만 이를 방문하도록 만들고.
# 동생이 움직이고 나서, 현재 시간의 홀,짝 여부를 판단하고 해당 배열의 방문 여부를 체크하고 방문 했다면 time을 출력해준다.
# 이렇게 함으로써, 왔던곳은 다시 방문을 하지 않지만, 왔다갔다를 반복해서 만나는 경우를 포함하게 된다.


def solve():
    global n, k, visited

    # 이미 위치가 같음
    if n == k:
        print(0)
        return

    q = deque([n])
    visited[0][n] = True
    time = 0
    while q:
        # 동생 위치 변경
        time += 1
        k += time

        if k > 500000:
            print(-1)
            return

        for _ in range(len(q)):
            cur = q.popleft()
            for next_position in (cur+1, cur-1, cur*2):
                # 정답
                if next_position == k:
                    print(time)
                    return

                if visited[time%2][k]:
                    print(time)
                    return

                if valid_position(next_position, time):
                    odd_or_even = time % 2
                    visited[odd_or_even][next_position] = True
                    q.append(next_position)


    print(-1)


def valid_position(position, time):
    global visited
    odd_or_even = time % 2
    return 0 <= position <= 500000 and not visited[odd_or_even][position]


n, k = map(int, sys.stdin.readline().strip().split(" "))
visited = [[False for _ in range(500001)] for _ in range(2)]
solve()