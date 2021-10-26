class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        global answer
        answer = -1

        def binSearch(left: int, right: int):
            global answer
            if left > right:
                answer = left
                return

            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                answer = mid
                return
            elif nums[mid] < target:
                binSearch(mid + 1, right)
            elif nums[mid] > target:
                binSearch(left, mid - 1)

        binSearch(0, len(nums) - 1)
        return answer