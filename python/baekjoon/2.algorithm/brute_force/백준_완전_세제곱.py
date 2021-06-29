import sys
# 문제를 잘 읽자 !!

def solve(target):
    ll = pow(target, 3)

    for i in range(2, 101):
        ii = pow(i, 3)
        if ii > ll:
            break

        for j in range(i, 101):
            jj = pow(j, 3)
            if jj > ll:
                break

            for k in range(j, 101):
                kk = pow(k, 3)
                if kk > ll:
                    break

                if ii + jj + kk == ll:
                    print("Cube = %d, Triple = (%d,%d,%d)" %(target, i, j, k))

for l in range(2, 101):
    solve(l)

