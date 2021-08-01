# 55 : 배열의 k번째 큰 요소
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k,nums)[-1]