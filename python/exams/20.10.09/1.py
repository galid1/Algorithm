def solution(N):
    dic = {}

    for i in range(2, 9):
        tn = N
        x = ''
        while tn:
            x = str(tn%i) + x
            tn //= i

        nx = list(map(int, x))
        res = 1
        for num in nx:
            if num:
                res *= num

        dic[i] = res

    dic = dict(sorted(dic.items(), reverse=True))
    max_ans = list(max(dic.items(), key = lambda item : item[1]))

    print(max_ans)
    return max_ans


solution(14)

