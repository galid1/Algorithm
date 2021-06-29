def solution(depar, hub, dest, roads):
    g = {}

    for road in roads:
        if road[0] not in g:
            g[road[0]] = [road[1]]
        else:
            g[road[0]].append(road[1])

    ans = []
    dfs(ans, depar, hub, dest, g, v_hub=False)
    print(len(ans))


def dfs(ans, depar, hub, dest, g, v_hub):
    if depar == dest:
        if v_hub:
            ans.append(1)
        return

    for li in g[depar]:
        if li == hub:
            v_hub = True

        dfs(ans, li, hub, dest, g, v_hub)

# def dfs(depar, hub, dest, g):
#     cnt = 0
#
#     stack = []
#     stack.append(depar)
#
#     # hub를 방문 했으며 마지막 정점이 dest이어야 함
#     visit_hub = False
#     while stack:
#         print(" ================= ")
#         cur_v = stack.pop()
#         print('stack: ', stack)
#         print('cur_v : ', cur_v)
#
#         if cur_v == hub:
#             print("visit !!")
#             visit_hub = True
#
#         # 현재 정점이 dest인 경우, hub를 방문했는지 확인하고 했으면 cnt += 1, hub방문을 초기화
#         if cur_v == dest:
#             print('cur_v: ', cur_v)
#             print('v_h: ', visit_hub)
#             if visit_hub:
#                 visit_hub = False
#                 cnt += 1
#             continue
#
#         for li in g[cur_v]:
#             print("push: ", li)
#             stack.append(li)
#
#
#
#     return cnt


solution("SEOUL", "DAEGU", "YEOSU", [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]])
# solution("ULSAN", "SEOUL", "BUSAN", [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]])