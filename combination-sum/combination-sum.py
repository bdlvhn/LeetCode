class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(nums: List[int], target: int):
            if target == 0:
                result.append(nums)
                return
            elif target < 0:
                return

            for i in range(len(candidates)):
                if not nums or nums[-1] <= candidates[i]:
                    dfs(nums + [candidates[i]], target-candidates[i])

        dfs([], target)

        return result
