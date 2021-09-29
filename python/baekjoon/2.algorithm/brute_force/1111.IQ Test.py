import sys


def solve():
    global n, data

    if n == 1:
        return print("A")

    if n == 2:
        if data[0] == data[1]:
            return print(data[0])
        else:
            return print("A")

    if data[0] - data[1] == 0:
        a = 0
    else:
        a = (data[1] - data[2]) // (data[0] - data[1])

    b = data[1] - data[0] * a

    for i in range(n-1):
        if data[i+1] != data[i] * a + b:
            return print("B")

    print(data[-1] * a + b)


n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()

# 5
# 3 6 12 24 48

# 4
# -10 10 -10 10

# 4
# -5 -4 -3 -2

# 4
# -1 -2 -3 -4

# 2
# 0 0

# 2
# 1 1

# 3
# 1 3 5

# 3
# 5 3 1

# 4
# 5 3 1 -1

# 3
# 3 1 0
