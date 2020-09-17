# 프로그래머스 Level 1 비밀지도

def solution(n, arr1, arr2):
    answer = []

    cypher_arr = []
    # 두개의 지도로 해독
    for i in range(n):
        cypher = bin(arr1[i] | arr2[i])[2:]
        cypher_arr.append(cypher)

    # 자리수 맞추기
    for i in range(n):
        cypher = cypher_arr[i]

        changed = False
        less_len = abs(len(cypher) - n)

        for j in range(less_len):
            cypher = '0' + cypher
            changed = True

        if changed:
            cypher_arr[i] = cypher

    for cypher in cypher_arr:
        cypher = list(cypher)
        plain = []

        for c in cypher:
            if c == '1':
                plain.append('#')
            else:
                plain.append(' ')

        answer.append(''.join(plain))

    return answer

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
