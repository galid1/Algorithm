import sys


def solve():
    global n, ss

    ans = []

    for s in ss:
        left = False
        right = False
        found = False
        for i in range(len(s)//2):
            if s[i] != s[len(s) - i - 1]:
                for j in range(i, len(s)//2):
                    if s[j+1] != s[len(s) - j - 1]:
                        left = True
                        break

                for j in range(i, len(s)//2):
                    if s[j] != s[len(s) - j - 2]:
                        right = True
                        break

                if left and right:
                    found = True
                    ans.append(2)
                    break
                elif left or right:
                    found = True
                    ans.append(1)
                    break

            if found:
                break

        if not found:
            ans.append(0)

    for a in ans:
        print(a)


def is_normal(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return True

    return False


n = int(sys.stdin.readline().strip())
ss = []

for _ in range(n):
    ss.append(list(sys.stdin.readline().strip()))

solve()