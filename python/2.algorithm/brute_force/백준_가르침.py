import sys


def solution(selected_count, start_idx):
    global n, k, max_count, arr, words

    if k < 5 or k == 26:
        print(0 if k < 5 else n)
        return

    if selected_count == k - 5:
        count = 0
        for word in words:
            for w in word:
                if not arr[ord(w) - ord('a')]:
                    break
            else:
                count += 1

        max_count = max(max_count, count)
        return

    for i in range(start_idx, len(arr)):
        if not arr[i]:
            arr[i] = 1
            solution(selected_count + 1, i+1)
            arr[i] = 0


# 정답
max_count = 0

n, k = map(int, sys.stdin.readline().strip().split(" "))
words = [set(sys.stdin.readline().strip()) for _ in range(n)]

arr = [False for i in range(26)]
for c in ('a', 'c', 'i', 'n', 't'):
    arr[ord(c) - ord('a')] = True

solution(0, 0)
print(max_count)