class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        def rotate(arr: List[int], start: int, end: int):
            while start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        rotate(nums, 0, len(nums)-1)
        rotate(nums, 0, k-1)
        rotate(nums, k, len(nums)-1)