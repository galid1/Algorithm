def solution(vs):
    x = 0
    y = 0

    fv = vs[0]
    sv = vs[1]
    tv = vs[2]

    if fv[0] == sv[0]:
        x = tv[0]
    elif fv[0] == tv[0]:
        x = sv[0]
    else:
        x = fv[0]

    if fv[1] == sv[1]:
        y = tv[1]
    elif fv[1] == tv[1]:
        y = sv[1]
    else:
        y = fv[1]

    return [x, y]

solution([[1, 4], [3, 4], [3, 10]])