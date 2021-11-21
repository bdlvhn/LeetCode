class Solution {
    public boolean canJump(int[] nums) {
        if (nums[0] == 0) {
            return nums.length == 1 ? true : false;
        }

        boolean[] reached = new boolean[nums.length];
        reached[0] = true;
        for (int i = 1; i < nums.length; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (reached[j] && nums[j] >= (i - j)) {
                    reached[i] = true;
                    break;
                }
            }
        }
        return reached[nums.length-1];
    }
}