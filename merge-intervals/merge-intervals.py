class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        deque = collections.deque(sorted(intervals))
        result = []
        
        while deque:
            now = deque.popleft()
            if not result:
                result.append(now)
            else:
                if result[-1][1] >= now[0]:
                    result[-1] = [min(result[-1] + now), max(result[-1] + now)]
                else:
                    result.append(now)
        return result