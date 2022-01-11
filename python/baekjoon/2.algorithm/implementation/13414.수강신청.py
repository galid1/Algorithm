import sys

k, l = map(int, sys.stdin.readline().strip().split(" "))
arr = {}

for i in range(l):
    st_id = sys.stdin.readline().strip()

    if st_id in arr.keys():
        arr.pop(st_id)

    arr[st_id] = i


for st_id in list(arr.keys())[:k]:
    print(st_id)