class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(A: List[int], B: List[int]):
            if not B:
                result.append(A)
                return

            for i in range(len(B)):
                if B[i] not in A:
                    dfs(A + [B[i]], B[:i] + B[i+1:])

        dfs([], nums)
        return result