class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        p = 1
        for num in nums:
            arr.append(p)
            p *= num

        p = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i] *= p
            p *= nums[i]
        
        return arr