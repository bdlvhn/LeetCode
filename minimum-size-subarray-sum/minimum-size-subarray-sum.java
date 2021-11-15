class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int result = 100000+1;
        int left = 0, right = 0;
        int sum = 0;
        while (right < nums.length) {
            sum += nums[right];
            if (sum >= target) {
                while (sum >= target) {
                    sum -= nums[left];
                    left++;
                }
                result = Math.min(result, right - left + 2);
            }
            right++;
        }
        return result == 100000+1 ? 0: result;
    }
}