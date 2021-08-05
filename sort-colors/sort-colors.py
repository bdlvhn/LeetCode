class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            while i > 0:
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    i -= 1
                else:
                    break