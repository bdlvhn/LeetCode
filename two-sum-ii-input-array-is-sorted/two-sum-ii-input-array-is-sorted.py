class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(left: int, right: int) -> int:
            if numbers[left] + numbers[right] > target:
                return binarySearch(left, right - 1)
            elif numbers[left] + numbers[right] < target:
                return binarySearch(left + 1, right)
            else:
                return [left + 1, right + 1]
        return binarySearch(0, len(numbers) - 1)