# 백준 1406 에디터
import sys

# 효율문제 시간초과
# def solution(s, commands):
#     # 0은 문장의 맨 앞, len - 1은 맨 뒤       0 1 2 3
#     # 인덱스의 앞에 커서가 위치한다고 가정 ex) [a,b,c,d]  cur_idx가 1인경우 커서는 a|b 에 위치함
#     cur_idx = len(s)
#
#     for cmd in commands:
#         if cmd == 'L':
#             if cur_idx == 0:
#                 continue
#             else:
#                 cur_idx -= 1
#
#         elif cmd == 'D':
#             if cur_idx == len(s):
#                 continue
#             else:
#                 cur_idx += 1
#
#         elif cmd == 'B':
#             if cur_idx == 0:
#                 continue
#             else:
#                 s = s[0:cur_idx-1] + s[cur_idx:]
#                 cur_idx = max(0, cur_idx - 1)
#
#         elif cmd[0] == 'P':
#             s = s[0:cur_idx] + [cmd[2]] + s[cur_idx:]
#             cur_idx = min(len(s) - 1, cur_idx + 1)
#
#     print(''.join(s))

def solution(s, commands):
    l = s
    r = []

    for cmd in commands:
        if cmd == 'L':
            if l:
                r.append(l.pop())
        elif cmd == 'D':
            if r:
                l.append(r.pop())
        elif cmd == 'B':
            if l:
                l.pop()
        elif cmd[0] == 'P':
            l.append(cmd[2])

    r.reverse()

    result = l + r
    result_str = ''.join(result)
    print(result_str)

s = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
commands = []
for i in range(n):
    commands.append(sys.stdin.readline().strip())

solution(s, commands)