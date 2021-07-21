class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        dist = collections.defaultdict(int)

        for a, b, c in times:
            graph[a].append((b, c))

        queue = [(0, k)]
        while queue:
            time, node = heapq.heappop(queue)
            if node not in dist:
                dist[node] = time
                for next, c in graph[node]:
                    cost = time + c
                    heapq.heappush(queue, (cost, next))

        return max(dist.values()) if len(dist) == n else -1