import sys


class Trie:
    def __init__(self):
        self.trie = {}

    def add(self, num):
        num = list(num)

        is_in = True
        c_trie = self.trie
        for c in num:
            if c not in c_trie.keys():
                is_in = False
                c_trie[c] = {}

            c_trie = c_trie[c]

        return is_in


def solve(nums):
    trie = Trie()

    for num in nums:
        is_in = trie.add(num)
        if is_in:
            return print("NO")
    print("YES")


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline())
    nums = []
    for _ in range(n):
        nums.append(sys.stdin.readline().strip())

    solve(sorted(nums, reverse=True))

