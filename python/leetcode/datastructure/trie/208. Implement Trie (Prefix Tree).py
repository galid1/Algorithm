# class Trie:
#     class TrieNode:
#         def __init__(self, c, is_end=False):
#             self.c = c
#             self.is_end = is_end
#
#         def __hash__(self):
#             return hash(self.c)
#
#         def __eq__(self, other):
#             return self.c == other
#
#     def __init__(self):
#         self.trie = {}
#
#     def __make_node__(self, c, idx=0, word_len=0):
#         trie_node = self.TrieNode(c)
#
#         if idx + 1 == word_len:
#             trie_node.is_end = True
#
#         return trie_node
#
#     def insert(self, word: str) -> None:
#         c_trie = self.trie
#         for idx, c in enumerate(list(word)):
#             trie_node = self.__make_node__(c, idx, len(word))
#
#             if trie_node not in c_trie.keys():
#                 c_trie[trie_node] = {}
#
#             # 마지막 글자
#             if trie_node.is_end:
#                 for key in c_trie:
#                     if c == key.c:
#                         key.is_end = True
#                         break
#
#             c_trie = c_trie[trie_node]
#
#     def search(self, word: str) -> bool:
#         c_trie = self.trie
#         for idx, c in enumerate(list(word)):
#             if idx == len(word) - 1:
#                 break
#
#             c_node = self.__make_node__(c)
#
#             if c_node in c_trie.keys():
#                 c_trie = c_trie[c_node]
#             else:
#                 break
#
#         if idx + 1 < len(word):
#             return False
#
#         for key in c_trie.keys():
#             if key.c == c and key.is_end:
#                 return True
#         return False
#
#     def startsWith(self, prefix: str) -> bool:
#         c_trie = self.trie
#         for idx, c in enumerate(list(prefix)):
#             c_node = self.__make_node__(c)
#
#             if c_node in c_trie.keys():
#                 c_trie = c_trie[c_node]
#             else:
#                 return False
#         return True


class Trie:
    class TrieNode:
        def __init__(self, c, children={}, word=False):
            self.c = c
            self.children = children
            self.word = word

        def __hash__(self):
            return hash(self.c)

        def __eq__(self, other):
            return self.c == other

    def __init__(self):
        self.trie = {}

    def __make_node__(self, c, idx, word_len):
        t_node = self.TrieNode(c)

        if idx+1 == word_len:
            t_node.word = True

        return t_node


    def insert(self, word: str) -> None:
        c_trie = self.trie
        word_len = len(word)

        for idx, c in enumerate(word):
            new_node = self.__make_node__(c, idx, word_len)
            if c not in c_trie.keys():
                c_trie[c] = new_node
            else:
                if idx+1 == word_len:
                    c_trie[c].word = True
                    break

            c_trie = c_trie[c].children


    def search(self, word: str) -> bool:
        c_trie = self.trie
        c_node = None
        for idx, c in enumerate(word):
            if c in c_trie.keys():
                c_node = c_trie[c]
                c_trie = c_node.children
                continue
            return False

        if not c_node:
            return False
        if c_node:
            if c_node.word:
                return True
            return False

    def startsWith(self, prefix: str) -> bool:
        c_trie = self.trie
        for idx, c in enumerate(prefix):
            if c not in c_trie.keys():
                return False
            c_trie = c_trie[c].children
        return True


obj = Trie()
# obj.insert("apple")
# print(obj.search("apple"))
# print(obj.search("app"))
# print(obj.search("ass"))
# print("====")
# print(obj.startsWith("app"))
# obj.insert("app")
# print(obj.search("app"))
# print(obj.search("apple"))
# print(obj.startsWith("a"))

obj.insert("abc")
print(obj.search("abc"))
print(obj.search("ab"))
obj.insert("ab")
print(obj.search("ab"))
obj.insert("ab")
print(obj.search("ab"))
