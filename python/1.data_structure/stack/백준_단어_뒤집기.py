import sys

def solve():
    global words

    sentence = ''
    for word in words:
        stack = []

        for c in word:
            stack.append(c)

        while stack:
            sentence += stack.pop()

        sentence += ' '

    print(sentence)

n = int(sys.stdin.readline().strip())
for _ in range(n):
    words = list(sys.stdin.readline().strip().split(" "))
    solve()

