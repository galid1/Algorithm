import queue

######## queue 생성시 변수 이름 queue로 하지 않기
######## 크기를 별도로 지정하지 않아도 속도차이 크게 없는듯
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())

if q.empty():
    print('y')

print(q.get())

if q.empty():
    print('y')