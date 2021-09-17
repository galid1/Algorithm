import sys

def solve():
    global s
    s.sort()

    answer = True
    idx = 0
    head = ''
    tail = ''
    skip = ''

    while idx < len(s):
        if idx == len(s)-1:
            if skip:
                answer = False
                break
            skip = s[idx]
            break

        if s[idx] != s[idx+1]:
            if len(s) % 2 == 0:
                answer = False
                break

            if skip:
                answer = False
                break

            skip = s[idx]
            idx += 1
            continue

        head += s[idx]
        tail = s[idx+1] + tail
        idx += 2

    if not answer:
        return print("I'm Sorry Hansoo")


    print(head, end='')
    if skip:
        print(skip, end='')
    print(tail)



s = list(sys.stdin.readline().strip())
solve()