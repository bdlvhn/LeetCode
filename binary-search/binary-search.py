class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start: int, end: int):
            if start > end:
                return -1
            
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binarySearch(start, mid-1)
            else:
                return binarySearch(mid+1, end)
        
        return binarySearch(0,len(nums)-1)