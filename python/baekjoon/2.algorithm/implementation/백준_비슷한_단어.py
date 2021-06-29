import sys, copy


def solve():
    global word, words

    word_len = len(word)
    ans = 0
    for cur_word in words:
        if abs(word_len - len(cur_word)) >= 2:
            continue

        word_cnt_copy = copy.deepcopy(word_cnt)
        for c in cur_word:
            word_cnt_copy[c] -= 1

        dif_cnt = 0
        similar = True
        for v in word_cnt_copy.values():
            dif_cnt += abs(v)
            if dif_cnt > 2:
                similar = False
                break

        if similar:
            ans += 1

    print(ans)


n = int(sys.stdin.readline().strip())
word = list(sys.stdin.readline().strip())
word_cnt = {chr(i): 0 for i in range(65, 65+26)}
for c in word:
    word_cnt[c] += 1

words = []
for _ in range(n-1):
    words.append(list(sys.stdin.readline().strip()))
solve()

# 10
# AAAB
# ABBA
# ABBB
# AAABC
# AAABB
# AABBB
# PABB
# ABCD
# AB
# ABAG