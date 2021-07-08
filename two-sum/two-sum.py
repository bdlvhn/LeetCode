class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            k = target - num
            if k in nums[i + 1:]:
                return [i, i + 1 + nums[i + 1:].index(k)]
