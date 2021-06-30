from collections import defaultdict

def mostCommonWord(paragraph, banned):
    banned = set(banned)
    words = []

    idx = -1
    while idx < len(paragraph):
        idx += 1

        temp_word, ci = '', idx
        while ci < len(paragraph) and paragraph[ci].isalpha():
            temp_word += paragraph[ci].lower()
            ci += 1
        idx = ci
        if temp_word:
            words.append(temp_word)

    cnts = {}
    for word in words:
        if word not in banned:
            if word in cnts.keys():
                cnts[word] += 1
            else:
                cnts[word] = 1

    return max(cnts.items(), key=lambda item: item[1])[0]


banned = ["hit"]
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
mostCommonWord(paragraph, banned)



