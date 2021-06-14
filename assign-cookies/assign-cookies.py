class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g = collections.deque(g)
        s = collections.deque(s)
        answer = 0
        while s and g:
            cookie = s.popleft()
            if g[0] <= cookie:
                g.popleft()
                answer += 1
        return answer