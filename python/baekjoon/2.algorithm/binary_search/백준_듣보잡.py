import sys


n, m = map(int, sys.stdin.readline().strip().split(" "))
ns = []
answers = []

for i in range(n):
    ns.append(sys.stdin.readline().strip())
ns.sort()

for j in range(m):
    temp = sys.stdin.readline().strip()
    s = 0
    e = len(ns)-1

    while s <= e:
        mid = (s+e)//2
        if temp == ns[mid]:
            answers.append(temp)
            break
        elif temp > ns[mid]:
            s = mid + 1
        else:
            e = mid - 1


# 결과 출력
answers.sort()
print(len(answers))
for a in answers:
    print(a)