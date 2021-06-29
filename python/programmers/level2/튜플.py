def solution(s):
    answer = []

    s = s[1:-1]
    ss = s.split("}")

    # ss(스플릿된 문자열)을 2차원 배열로 만듦
    tuples = []
    for line in ss:
        if line:
            idx = 0
            tup = []
            while idx < len(line):
                num = ''
                while idx < len(line) and not line[idx].isdigit():
                    idx += 1
                while idx < len(line) and line[idx].isdigit():
                    num += line[idx]
                    idx += 1
                tup.append(int(num))
            tuples.append(tup)

    # 2차원 배열을 길이를 기준으로 정렬
    tuples.sort(key= lambda x : len(x))

    for tup in tuples:
        tl = list(set(tup).difference(set(answer)))
        answer += tl

    return answer


# solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
# solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")