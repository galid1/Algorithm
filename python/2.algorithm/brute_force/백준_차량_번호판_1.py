import sys

def solution():
    global s
    cur = 1
    bef = ''
    for c in s:
        if c == 'c':
            operand = 26
            if bef == 'c':
                operand -= 1
            cur *= operand
            bef = 'c'
        else:
            operand = 10
            if bef == 'd':
                operand -= 1
            cur *= operand
            bef = 'd'

    print(cur)


s = list(sys.stdin.readline().strip())
solution()