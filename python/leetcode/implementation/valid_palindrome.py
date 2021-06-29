def isPalindrome(s: str) -> bool:
    s = get_only_char(s.lower())

    if not s:
        return True

    for i in range(len(s)//2+1):
        if s[i] != s[len(s)-1-i]:
            return False

    return True


def get_only_char(s):
    only_c = ''
    for c in s:
        if c.isalpha() or c.isnumeric():
            only_c += c
    return only_c


print(isPalindrome("0P"))