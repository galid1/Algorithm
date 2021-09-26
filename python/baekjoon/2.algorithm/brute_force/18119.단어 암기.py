import sys

def solve():
    global n, m, words, cmds

    word_memory = []

    for word in words:
        cur_bit = 0
        for c in set(word):
            cur_bit += 1 << (ord(c) - 97)

        word_memory.append(cur_bit)

    bit_mask = (1 << 26) - 1
    for o, x in cmds:
        c_bit = 1 << (ord(x) - 97)
        if o == '1':
            bit_mask -= c_bit
        else:
            bit_mask += c_bit

        res = 0
        for word in word_memory:
            if word == word & bit_mask:
                res += 1
        print(res)


n, m = map(int, sys.stdin.readline().strip().split(" "))
words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip())

cmds = []
for _ in range(m):
    cmds.append(sys.stdin.readline().strip().split(" "))

solve()