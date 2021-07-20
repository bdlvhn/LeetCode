class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(arr: List[int], nums: List[int]):
            subsets.append(arr)
            if not nums:
                return
            
            for i in range(len(nums)):
                if not arr or arr[-1] < nums[i]:
                    dfs(arr + [nums[i]], nums[:i] + nums[i+1:])

        dfs([], nums)
        return subsets