class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int count = 0;
        //nums = [10,5,2,6], k = 100
        for (int i = 0; i < nums.length; i++) {
            int numberSum = 1;
            for (int j = i; j < nums.length; j++) {
                numberSum *= nums[j];
                if (numberSum >= k) break;
                count++;
            }
        }
        return count;
    }
}