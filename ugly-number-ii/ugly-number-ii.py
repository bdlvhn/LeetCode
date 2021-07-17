class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = [1]
        cnt = 1

        while cnt < n:
            now = heapq.heappop(q)
            for i in [2, 3, 5]:
                if now * i not in q:
                    heapq.heappush(q, now * i)
            cnt += 1

        return heapq.heappop(q)