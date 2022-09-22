class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        import heapq
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        queue = [(0, k)]
        dist = defaultdict(int)
        while queue:
            time, node = heapq.heappop(queue)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    heappush(queue, (time + w, v))
        
        if len(dist) == n:
            return max(dist.values())
        return -1