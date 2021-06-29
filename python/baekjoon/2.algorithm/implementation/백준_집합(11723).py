import sys

def solve(args):
    global nums

    cmd = args[0]

    if cmd == "add":
        x = args[1]
        nums[int(x)] = 1

    elif cmd == "check":
        x = args[1]
        if nums[int(x)]:
            print(1)
        else:
            print(0)

    elif cmd == "remove":
        x = args[1]
        nums[int(x)] = 0

    elif cmd == "toggle":
        x = args[1]
        nums[int(x)] = 1 - nums[int(x)]

    elif cmd == "all":
        nums = [1 for _ in range(21)]

    elif cmd == "empty":
        nums = [0 for _ in range(21)]


nums = [0 for _ in range(21)]
n = int(sys.stdin.readline().strip())
for _ in range(n):
    solve(sys.stdin.readline().strip().split(" "))
