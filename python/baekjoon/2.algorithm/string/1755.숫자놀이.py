import sys, heapq


def solve():
    global n, m

    ans = []
    for num in range(n, m+1):
        str_num = get_str(num)
        heapq.heappush(ans, [str_num, num])

    idx = 0
    while ans:
        cur = heapq.heappop(ans)[1]
        print(cur, end=' ')
        idx += 1

        if idx%10 == 0:
            print()


def get_str(num):
    global num_alpha

    res = ''
    for c in list(str(num)):
        res += num_alpha[c]

    return res

n, m = map(int, sys.stdin.readline().strip().split(" "))
num_alpha = {
    '0': "ze",
    '1': "on",
    '2': "tw",
    '3': "th",
    '4': "fo",
    '5': "fi",
    '6': "si",
    '7': "se",
    '8': "ei",
    '9': "ni"
}
solve()