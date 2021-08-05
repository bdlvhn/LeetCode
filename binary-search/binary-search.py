class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        mid = (left + right) // 2
        while left <= mid <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            if mid == (left + right) // 2:
                return -1
            mid = (left + right) // 2