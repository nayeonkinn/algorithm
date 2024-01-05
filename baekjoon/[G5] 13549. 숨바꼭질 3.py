import heapq

# n, k = 5, 17  # 2
n, k = map(int, input().split())

def dijkstra(n, k):
    if n > k:  # 수빈 위치가 더 큰 경우 -1씩 이동할 수밖에 없으므로 따로 처리
        return n - k

    queue = []
    heapq.heappush(queue, (0, n))

    costs = [1e9] * 100001
    costs[n] = 0

    while queue:
        time, pos = heapq.heappop(queue)

        if pos == k:
            return time
        
        for np, nt in ((2 * pos, time), (pos - 1, time + 1), (pos + 1, time + 1)):
            if 0 <= np <= 100000 and costs[np] > nt:
                costs[np] = nt
                heapq.heappush(queue, (nt, np))

print(dijkstra(n, k))