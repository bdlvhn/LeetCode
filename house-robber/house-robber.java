class Solution {
    public int rob(int[] nums) {
        if (nums.length <= 2) return Arrays.stream(nums).max().getAsInt();
        
        nums[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++) { 
            nums[i] = nums[i] + nums[i-2] < nums[i-1] ? nums[i-1] : nums[i] + nums[i-2];
        }
        
        return nums[nums.length-1];
    }
}