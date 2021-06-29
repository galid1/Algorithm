import sys
sys.setrecursionlimit(20000)

def post_order(start, end):
     global tree

     # 원소가 1개 일때 까지만
     if start > end:
          return

     division = start+1
     for i in range(start+1, end+1):
          if tree[i] > tree[start]:
               division = i
               break

     post_order(start+1, division-1)
     post_order(division, end)

     print(tree[start])


tree = []
while True:
     val = sys.stdin.readline().strip()

     # eof
     if not val:
          break

     # tree에 추가
     tree.append(int(val))

post_order(0, len(tree)-1)



# 50
# 30
# 24
# 5
# 28
# 45
# 98
# 52
# 60

# start = 0, end = len(tree)-1
# division = start+1 부터


