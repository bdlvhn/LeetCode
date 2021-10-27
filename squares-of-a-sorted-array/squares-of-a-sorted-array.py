class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            heapq.heappush(arr, num ** 2)

        result = []
        while arr:
            result.append(heapq.heappop(arr))
        return result