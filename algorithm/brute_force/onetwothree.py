import sys

def use_one_two_three(n, current_sum = 0):
    global count

    if current_sum is n:
        count += 1
        return

    if current_sum > n :
        return

    for i in range(1, 4):
        use_one_two_three(n, current_sum + i)


count = 0
n = int(sys.stdin.readline().strip())
use_one_two_three(n)
print(count)
