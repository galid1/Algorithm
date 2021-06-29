import sys

def solve():
    global brackets

    stack = []
    for c in brackets:
        if is_open(c):
            stack.append(c)
        else:
            # 올바르지 못한 식
            if not stack:
                print(0)
                return
            else:
                temp = 0
                pop = stack.pop()

                while stack and type(pop) == int:
                    temp += pop
                    pop = stack.pop()

                if is_pair(c, pop):
                    operand = 3 if c == ']' else 2

                    if temp == 0:
                        stack.append(operand)
                    else:
                        stack.append(temp * operand)

                else:
                    print(0)
                    return

    ans = 0
    while stack:
        pop = stack.pop()
        if type(pop) != int:
            print(0)
            return
        else:
            ans += pop

    print(ans)


def is_open(bracket):
    if bracket == '(' or bracket == '[':
        return True
    return False

def is_pair(cur, pop):
    global pairs
    if pop == pairs[cur]:
        return True
    return False

pairs = {
    ')': '(',
    ']': '['
}
brackets = list(sys.stdin.readline().strip())
solve()


# (([])[()])()