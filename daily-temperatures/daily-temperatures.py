class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for idx, t in enumerate(temperatures):
            if not stack:
                stack.append(idx)
            else:
                while stack and temperatures[stack[-1]] < t:
                    answer[stack[-1]] = idx - stack[-1]
                    stack.pop()
                stack.append(idx)

        return answer