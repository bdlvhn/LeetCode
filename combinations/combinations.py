class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(A: List[int], B: List[int]):
            if len(A) == k:
                result.append(A)
                return

            for i in range(len(B)):
                if not A or A[-1] < B[i]:
                    dfs(A + [B[i]], B[:i] + B[i+1:])

        dfs([], [i for i in range(1, n+1)])

        return result