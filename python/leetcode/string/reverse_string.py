def reverseString(s) -> None:
    ns = ''
    for i in range(len(s)-1, -1, -1):
        ns += s[i]

    s = ns

# s = ["h","e","l","l","o"]
# s = "A man, a plan, a canal: Panama"
# "amanaP :lanac a ,nalp a ,nam A"


s = ["A", "B", "D", " ", " ", "C"]
reverseString(s)

