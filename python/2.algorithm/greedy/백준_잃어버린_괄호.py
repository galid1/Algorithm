import sys

def solution(s):
    arr = list(s.split("-"))
    if not arr[0]:
        arr[1] = '-' + arr[1]
        arr = arr[1:]

    arr = [sum(list(map(int, n.split("+")))) for n in arr]

    ans = arr[0]
    for i in range(1, len(arr)):
        ans -= arr[i]

    print(ans)


s = sys.stdin.readline().strip()
solution(s)
