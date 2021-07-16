class Solution:
    def isValid(self, s: str) -> bool:
        s = collections.deque(s)
        dict = {}
        dict[')'], dict[']'], dict['}'] = '(', '[', '{'
        stack = []
        
        while s:
            now = s.popleft()
            if now in ['(','[','{']:
                stack.append(now)
            else:
                if not stack or dict[now] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack