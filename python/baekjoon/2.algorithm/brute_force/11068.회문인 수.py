import sys


def solve(n):
    if is_palindrome(list(str(n))):
        return print(1)

    idx = 2
    while idx <= 64 and idx < n:
        changed_n = change(n, idx)

        if is_palindrome(changed_n):
            return print(1)

        idx += 1

    print(0)


def is_palindrome(n):
    for i in range(len(n)//2 + 1):
        if n[i] != n[len(n) - 1 - i]:
            return False

    return True


def change(num, n):
    result = []

    while num:
        result.append(str(num%n))
        num //= n

    return result


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    solve(n)