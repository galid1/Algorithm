#프로그래머스 스킬체크 lv2. 1
# Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
#
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

import sys

def number_of_presentation(n):
    count = 1

    for i in range((n//2)+1):
        temp = n
        for j in range(i+1, (n//2)+2):
            temp -= j
            if temp == 0:
                count += 1
                break
            if temp < 0:
                break

    print(count)


n = int(sys.stdin.readline())
number_of_presentation(n)