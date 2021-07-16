class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        product_1, product_2 = itertools.product(nums1, nums2), itertools.product(nums3, nums4)
        dict_1, dict_2 = collections.defaultdict(int), collections.defaultdict(int)
        for res in product_1:
            dict_1[sum(res)] += 1
        for res in product_2:
            dict_2[sum(res)] += 1
        
        for key in dict_1:
            if -1 * key in dict_2:
                count += dict_1[key] * dict_2[-1 * key]
        return count