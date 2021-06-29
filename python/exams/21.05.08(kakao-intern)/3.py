def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    k += 1
    deleted = []

    for c in cmd:
        # 이동 명령
        if len(c) == 3:
            direction, cnt = c.split(" ")
            cnt = int(cnt)

            if direction == 'D':
                k += cnt
            elif direction == 'U':
                k -= cnt

        # 삭제
        elif c == 'C':
            deleted.append(k-1)
            if k == n:
                k -= 1
            n -= 1

        # 복구
        elif c == 'Z':
            if deleted[-1] <= k:
                k += 1
            n += 1
            deleted.pop()

    for d_idx in deleted:
        answer[d_idx] = 'X'

    res = ''
    for ans in answer:
        res += ans

    return res


# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
solution(8, 2, cmd)
