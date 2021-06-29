def solution(s, n):
    strs = list(s)

    for i in range(len(strs)):
        cur_c = strs[i]

        if cur_c.isupper():
            strs[i] = chr((ord(cur_c) - 65 + n)%26 + 65)
        elif cur_c.islower():
            strs[i] = chr((ord(cur_c) - 97 + n)%26 + 97)

    return ''.join(strs)


solution("AB", 1)
print(solution("c B", 1))

