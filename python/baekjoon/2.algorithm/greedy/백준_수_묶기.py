import sys

def solution():
    global n, arr
    arr.sort()
    ans = 0

    # 음수 처리
    left = 0
    for i in range(0, len(arr)-1, +2):
        if arr[i] < 1 and arr[i+1] < 1:
            ans += arr[i] * arr[i+1]
            left += 2
        else:
            break

    # 양수 처리
    right = len(arr) - 1
    for j in range(len(arr)-1, 0, -2):
        if arr[j] > 1 and arr[j-1] > 1:
            ans += arr[j] * arr[j-1]
            right -= 2
        else:
            break

    for k in range(left, right+1):
        ans += arr[k]

    print(ans)

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
solution()