class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 해시 사용
        nums_map = {}
        for i,num in enumerate(nums):
            if target-num in nums_map:
                return [i,nums_map[target-num]]
            nums_map[num] = i