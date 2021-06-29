def solution(s):
    answer = True

    lower_s = s.lower()

    p_count = 0
    y_count = 0

    for c in lower_s:
        if c == 'p':
            p_count += 1
        if c == 'y':
            y_count += 1

    if p_count != y_count:
        answer = False

    return answer

solution('pPoooyY')
