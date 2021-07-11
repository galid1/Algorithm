def removeDuplicateLetters(s):
    cnts = make_cnts(s)
    visited = set()
    stack = []

    for c in s:
        cnts[c] -= 1

        if c in visited:
            continue

        if not stack:
            stack.append(c)
            visited.add(c)
            continue

        top_c = stack[-1]
        while stack and top_c > c and cnts[top_c] >= 1:
            visited.remove(top_c)
            stack.pop()

            if stack:
                top_c = stack[-1]

        visited.add(c)
        stack.append(c)


    return ''.join(stack)


def make_cnts(s):
    cnts = {}

    for c in s:
        if c not in cnts.keys():
            cnts[c] = 1
        else:
            cnts[c] += 1

    return cnts


# s = "bcabc"
# s = "bcabcdb"
# s = "cbacdcbc"
# s = "aaaabcacd"
# s = "abcabc"
s = "abacb"
print(removeDuplicateLetters(s))
