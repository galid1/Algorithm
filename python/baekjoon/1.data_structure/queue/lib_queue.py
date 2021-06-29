#hackerrank Queue using Two Stacks
import sys
import queue

######## queue 생성시 변수 이름 queue로 하지 않기
######## 크기를 별도로 지정하지 않아도 속도차이 크게 없는듯


n = int(sys.stdin.readline())
execute = []
q = queue.Queue()

for i in range(n):
    execute.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

for i in execute:
    if i[0] == 1:
        q.put(i[1])
    elif i[0] == 2:
        q.get()
    elif i[0] == 3:
        print(q.queue[0])