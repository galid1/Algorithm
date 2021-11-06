def solution(s):
    answer = []
    visited = [False for _ in range(len(s))]

    idx, cnt = cal_start(s, visited)
    answer.append(cnt)

    while idx < len(s):
        if visited[idx]:
            idx += 1
            continue

        cur_c = s[idx]
        cnt = 1
        c_idx = idx+1

        while c_idx < len(s):
            if visited[c_idx] or cur_c != s[c_idx]:
                break

            cnt += 1
            c_idx += 1

        answer.append(cnt)
        idx = c_idx

    answer.sort()
    return answer


def cal_start(s, v):
    cur_c = s[0]
    v[0] = True

    idx = 1
    cnt = 1
    while idx < len(s):
        if s[idx] != cur_c:
            break

        cnt += 1
        v[idx] = True
        idx += 1

    r_idx = -1
    while len(s) + r_idx > idx:
        if s[r_idx] != cur_c:
            break

        cnt += 1
        v[r_idx] = True
        r_idx -= 1

    return idx, cnt



s = "aaabbaaa"
s = "wowwow"
# s = "baaab"
# s = "aaabaa"
# s = "abaabaa"
# s = "aaa"
# s = "a"
# s = "ba"
# s = "abcdefga"
print(solution(s))