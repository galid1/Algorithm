import sys


def solve():
    global n, mapping

    # 3의 배수만들기
    while len(n) % 3 != 0:
        n = '0'+ n

    ans = ''
    for i in range(len(n)//3):
        start_i = i*3
        key = n[start_i: start_i+3]
        ans += mapping[key]

    print(ans)



mapping = {
    '000': '0',
    '001': '1',
    '010': '2',
    '011': '3',
    '100': '4',
    '101': '5',
    '110': '6',
    '111': '7'
}
n = sys.stdin.readline().strip()
solve()


# 000	0
# 001	1
# 010	2
# 011	3
# 100	4
# 101	5
# 110	6
# 111	7