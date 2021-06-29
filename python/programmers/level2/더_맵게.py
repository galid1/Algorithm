import heapq

def solution(scoville, k):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) > 1 and scoville[0] < k:
        answer += 1
        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)

        # 새로운 스코빌 넣기
        new_one = fir + (sec * 2)
        heapq.heappush(scoville, new_one)

    if scoville[0] < k:
        return -1

    return answer

solution([1, 2, 3, 9, 10, 12], 7)
solution([1, 2], 3)
solution([1, 2], 10)