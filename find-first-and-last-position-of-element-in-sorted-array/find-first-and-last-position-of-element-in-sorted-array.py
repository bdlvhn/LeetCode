class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx_left = self.findFirstIndex(nums, target)
        if idx_left == len(nums) or nums[idx_left] != target:
            return [-1, -1]
        return [idx_left, self.findFirstIndex(nums, target+1) - 1]

    def findFirstIndex(self, nums: List[int], target: int):
        low, high = 0, len(nums)

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low