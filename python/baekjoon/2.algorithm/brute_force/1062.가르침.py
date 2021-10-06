import sys
from itertools import combinations


def solve():
    global n, k, words

    if k < 5:
        return print(0)

    # bit 마스크 설정 (a, n, i, c, t 는 무조건 알아야 함)
    knows = on_bit(['a', 'n', 'i', 'c', 't'])

    alphas = [chr(i) for i in range(97, 97 + 26)]
    alphas.remove('a')
    alphas.remove('n')
    alphas.remove('c')
    alphas.remove('i')
    alphas.remove('t')

    ans = 0
    for selected in combinations(alphas, k-5):
        knows |= on_bit(selected)
        ans = max(ans, cal_know_words(knows))
        knows = off_bit(knows, selected)

    print(ans)


def cal_know_words(knows):
    global words
    result = 0

    for word in words:
        if knows & word == word:
            result += 1

    return result


def on_bit(alphas):
    result = 0
    for c in alphas:
        cur = 1 << (ord(c) - 97)
        result |= cur

    return result


def off_bit(knows, alphas):
    for c in alphas:
        cur = 1 << (ord(c) - 97)
        knows ^= cur

    return knows


n, k = map(int, sys.stdin.readline().strip().split(" "))
words = []
for _ in range(n):
    words.append(on_bit(list(sys.stdin.readline().strip())))

solve()

# 0b10000010000100000101