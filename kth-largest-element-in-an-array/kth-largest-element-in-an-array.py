# 55 : 배열의 k번째 큰 요소
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x : -x, nums))
        heapq.heapify(nums)

        while k > 1:
            a = heapq.heappop(nums)
            k -= 1

        return -1 * heapq.heappop(nums)