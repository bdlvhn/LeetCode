class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                new_target = target - (nums[i] + nums[j])
                dict = collections.defaultdict(int)
                for k in range(j + 1, len(nums)):
                    if new_target - nums[k] in dict:
                        if [nums[i], nums[j], nums[k], new_target - nums[k]] not in answer:
                            answer.append([nums[i], nums[j], nums[k], new_target - nums[k]])
                    dict[nums[k]] += 1

        return answer