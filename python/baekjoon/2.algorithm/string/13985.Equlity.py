import sys

def solve(strs):
    adder, res = map(int, strs[1].split("="))

    if int(strs[0]) + adder == res:
        print("YES")
    else:
        print("NO")


strs = sys.stdin.readline().strip().split("+")
solve(strs)