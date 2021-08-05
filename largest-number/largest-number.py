class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def to_swap(s1: int, s2: int) -> bool:
            return str(s1) + str(s2) < str(s2) + str(s1)

        for i in range(len(nums)):
            j = i
            while j > 0 and to_swap(nums[j-1], nums[j]):
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
        return str(int(''.join(map(str,nums))))