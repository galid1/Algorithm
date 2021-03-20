def solution(inp_str):
    answer = []
    alpha_sm = [chr(i) for i in range(97, 123)]
    alpha_big = [chr(i) for i in range(65, 91)]
    nums = [str(i) for i in range(10)]
    specific = ["~", "!", "@", "#", "$", "%", "^", "&", "*"]

    fir_cond(inp_str, answer)
    sec_cond(inp_str, answer, alpha_sm, alpha_big, nums, specific)
    thi_cond(inp_str, answer, alpha_sm, alpha_big, nums, specific)
    for_cond(inp_str, answer)
    fif_cond(inp_str, answer)

    answer.sort()
    if not answer:
        answer.append(0)
    print(answer)
    return answer

def fir_cond(inp_str, ans):
    if len(inp_str) < 8 or len(inp_str) > 15:
        ans.append(1)

def sec_cond(inp_str, ans, alpha_sm, alpha_big, nums, specific):
    for c in inp_str:
        if c not in alpha_sm and c not in alpha_big and c not in nums and c not in specific:
            ans.append(2)
            break

def thi_cond(inp_str, ans, alpha_sm, alpha_big, nums, specific):
    contain_map = {1: False, 2: False, 3: False, 4: False}

    for c in inp_str:
        # a ~ z
        if c in alpha_sm:
            contain_map[1] = True
            continue
        # A ~ Z
        if c in alpha_big:
            contain_map[2] = True
            continue
        # 0~9
        if c in nums:
            contain_map[3] = True
            continue
        if c in specific:
            contain_map[4] = True

    cnt = 0
    for i in range(1, 5):
        if contain_map[i]:
            cnt += 1

    if cnt < 3:
        ans.append(3)

def for_cond(inp_str, ans):
    cur_c = ''
    cur_cnt = 0
    for c in inp_str:
        if cur_cnt >= 4:
            ans.append(4)
            break

        if cur_c != c:
            cur_c = c
            cur_cnt = 1
        else:
            cur_cnt += 1

def fif_cond(inp_str, ans):
    counts = {}

    for c in inp_str:
        if c in counts.keys():
            counts[c] += 1
        else:
            counts[c] = 1

    counts = sorted(counts.values(), reverse=True)

    if counts[0] >= 5:
        ans.append(5)

solution("AaTa+!12-3")
solution("aaaaZZZZ)")
solution("CaCbCgCdC888834A")
solution("UUUUU")
solution("ZzZz9Z824")