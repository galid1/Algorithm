import sys


def solution():
    global n

    # 모음 1개부터 시작
    v_c = 1
    while True:
        # 모음을 위 개수 만큼 선택하고 선택할 수 있는 자음의 수 파악
        c_c = n - v_c
        # 자음의 수가 2개 밑으로 선택 가능하면 그만
        if c_c < 2:
            break

        select_vs(v_c, [], 0, c_c)
        v_c += 1


def select_vs(v_c, vs, v_start, c_c):
    global vowel

    if len(vs) == v_c:
        select_cs(vs, c_c, [], 0)
        return

    for i in range(v_start, len(vowel)):
        vs.append(vowel[i])
        select_vs(v_c, vs, i+1, c_c)
        vs.pop()


def select_cs(vs, c_c, cs, c_start):
    global consonant, answers

    if len(cs) == c_c:
        ans = ''.join(list(sorted(vs + cs)))
        answers.append(ans)
        return

    for i in range(c_start, len(consonant)):
        cs.append(consonant[i])
        select_cs(vs, c_c, cs, i+1)
        cs.pop()


answers = []
n, m = map(int, sys.stdin.readline().strip().split(" "))
vowel = []
consonant = []
vowel_const = ['a', 'i', 'o', 'u', 'e']

arr = list(sys.stdin.readline().strip().split(" "))
for c in arr:
    if c in vowel_const:
        vowel.append(c)
    else:
        consonant.append(c)

solution()
answers.sort()
for ans in answers:
    print(ans)