import sys


def solution():
    global t, ns, ms
    s_ns, s_ms = [], []
    c_s_ns, c_s_ms = {}, {}

    # 부분합 구하기 및 수 세기
    cal_sub_sums(ns, s_ns)
    for s in s_ns:
        c_s_ns[s] = c_s_ns[s] + 1 if s in c_s_ns.keys() else 1
    cal_sub_sums(ms, s_ms)
    for s in s_ms:
        c_s_ms[s] = c_s_ms[s] + 1 if s in c_s_ms.keys() else 1

    set_ns, set_ms = list(set(s_ns)), list(set(s_ms))

    ans = 0
    for k in c_s_ns.keys():
        if t - k in c_s_ms.keys():
            ans += c_s_ns[k] * c_s_ms[t-k]



    print(ans)

def cal_sub_sums(num_list, sums_store):
    for i in range(0, len(num_list)):
        sums = 0
        for j in range(i, len(num_list)):
            sums += num_list[j]
            sums_store.append(sums)


t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
ns = list(map(int, sys.stdin.readline().strip().split(" ")))
m = int(sys.stdin.readline())
ms = list(map(int, sys.stdin.readline().strip().split(" ")))
solution()

