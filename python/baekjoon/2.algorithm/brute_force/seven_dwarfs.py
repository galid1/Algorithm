# baekjoon 2309번 일곱 난쟁이

import sys

def seven_dwarfs(dwarfs):
    for i in range(0,8):
        for j in range(i+1, 9):
            height_sum = []
            for k in range(0,9):
                if k == i or k == j:
                    continue
                height_sum.append(dwarfs[k])

            if sum(height_sum) == 100:
                height_sum.sort()
                for g in height_sum:
                    print(g)
                return


dwarfs = []
for i in range(9):
    dwarfs.append(int(sys.stdin.readline()))
seven_dwarfs(dwarfs)