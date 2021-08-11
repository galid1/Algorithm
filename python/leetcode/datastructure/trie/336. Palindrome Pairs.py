from collections import defaultdict

class TrieNode:
    def __init__(self, idx=-1):
        self.children = defaultdict(TrieNode)
        self.idx = idx
        self.palindrome_ids = []

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def append(self, s, s_idx):
        # 트라이에 넣기
        c_trie = self.trie

        for idx, c in enumerate(reversed(s)):
            if self.is_palindrome(s[0:len(s)-idx]):
                c_trie.palindrome_ids.append(s_idx)
            c_trie = c_trie.children[c]

        c_trie.idx = s_idx

    def is_palindrome(self, word):
        if not word:
            return False

        for idx in range(len(word) // 2):
            if word[idx] != word[len(word) - idx - 1]:
                return False

        return True

    def get_pair(self, word, word_idx):
        pairs = []

        # word가 더 길고 word의 나머지가 팰린드롬인 경우
        c_trie = self.trie
        while word:
            if c_trie.idx >= 0 and self.is_palindrome(word):
                pairs.append([word_idx, c_trie.idx])

            if word[0] not in c_trie.children:
                return pairs
            c_trie = c_trie.children[word[0]]
            word = word[1:]

        # idx >= 0
        if c_trie.idx >= 0 and c_trie.idx != word_idx: #lll 과 같이 전 글자가 같은 경우 대비
            pairs.append([word_idx, c_trie.idx])

        # 나머지가 팰린드롬
        for p_idx in c_trie.palindrome_ids:
            pairs.append([word_idx, p_idx])

        return pairs


class Solution:
    def __init__(self):
        self.trie = Trie()

    def palindromePairs(self, words):
        self.make_trie(words)

        ans = []
        for idx, word in enumerate(words):
            ans += self.trie.get_pair(word, idx)

        return ans

    def make_trie(self, words):
        for idx, word in enumerate(words):
            self.trie.append(word, idx)


s = Solution()
# words = ["bat","tab","cat"]
words = ["lls","sl", 's', 'ls', 'll', 'l']
s.palindromePairs(words)

# a = [[1,2], [3,4]]
# b = [[3,4], [4,5]]
# c = a + b
# print(c)