def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]

    if sticky:
        do_sticky(answer, servers, requests)
    else:
        do_normal_rr(answer, servers, requests)

    return answer


def do_normal_rr(answer, servers, requests):
    for idx, req in enumerate(requests):
        server_idx = idx % servers
        answer[server_idx].append(req)



def do_sticky(answer, servers, requests):
    bef_request_map = {}

    req_idx, server_idx = -1, -1
    while req_idx < len(requests)-1:
        req_idx += 1

        cur_req = requests[req_idx]

        mapped_server_idx = get_mapping_server(cur_req, bef_request_map)
        if mapped_server_idx != -1:
            answer[mapped_server_idx].append(cur_req)
            continue

        # 이전에 맵핑된것이 없는 경우
        server_idx = (server_idx+1) % servers
        bef_request_map[cur_req] = server_idx
        answer[server_idx].append(cur_req)


def get_mapping_server(cur_req, bef_request_map):
    if cur_req in bef_request_map.keys():
        return bef_request_map[cur_req]

    return -1


servers = 2
requests = [1,2,3,4]
sticky = False
print(solution(servers, sticky, requests))


servers = 2
requests = [1,1,2,2]
sticky = True
print(solution(servers, sticky, requests))