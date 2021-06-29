import sys


def solve():
    global n, ex
    ans = []
    max_num = 0

    for people in patterns.keys():
        cnt = 0
        pattern = patterns[people]
        pl = len(pattern)

        for i in range(n):
            if ex[i] == pattern[i%pl]:
                cnt += 1

        ans.append((people, cnt))
        max_num = max(max_num, cnt)

    print(max_num)
    for people, cnt in ans:
        if cnt == max_num:
            print(people)



n = int(sys.stdin.readline().strip())
ex = list(sys.stdin.readline().strip())
patterns = {
    'Adrian': ['A', 'B', 'C'],
    'Bruno': ['B', 'A', 'B', 'C'],
    'Goran': ['C', 'C', 'A', 'A', 'B', 'B']
}
solve()