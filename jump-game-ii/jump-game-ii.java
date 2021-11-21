class Solution {
    public int jump(int[] nums) {
        if (nums.length == 1) return 0;
        
        int[] steps = new int[nums.length];
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = 1; j <= nums[i]; j++) {
                if (i+j >= nums.length) break;
                if (steps[i+j] == 0) {
                    steps[i+j] = steps[i] + 1;
                } else {
                    steps[i+j] = Math.min(steps[i+j], steps[i] + 1);
                }
            }
        }
        return steps[nums.length-1];
    }
}