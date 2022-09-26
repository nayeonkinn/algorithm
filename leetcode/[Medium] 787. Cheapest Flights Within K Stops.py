class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict
        from collections import deque
        
        graph = defaultdict(list)
        for s, e, p in flights:
            graph[s].append((e, p))
        
        queue = deque([(0, src, k)])
        min_price = [1e9] * n
        while queue:
            price, node, cnt = queue.popleft()
            if node == dst:
                continue
            if cnt >= 0:
                for e, p in graph[node]:
                    if price + p < min_price[e]:
                        min_price[e] = price + p
                        queue.append((price + p, e, cnt - 1))
        
        if min_price[dst] == 1e9:
            return -1
        else:
            return min_price[dst]