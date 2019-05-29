# 백준 11053번 가증 긴 증가하는 부분 수열

import sys
import collections

def longest_increasing_subsequence(s, n):
    d[1] = 1

    for i in range(2, len(s)):
        d[i] = 1

        for j in range(i-1, 0, -1):
            if s[i] > s[j] :
                d[i] = max(d[i], 1+d[j])

    print(max(d))

n = int(sys.stdin.readline())
sequence = collections.deque(list(map(int, sys.stdin.readline().rstrip().split(" "))))
sequence.appendleft(0)
d = [0 for i in range(1001)]
longest_increasing_subsequence(sequence, n)
