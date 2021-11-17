class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        findSubset(nums, result, new ArrayList<>(), 0, nums.length);
        return result;
    }

    private void findSubset(int[] nums, List<List<Integer>> result, List<Integer> route, int start, int end) {
        result.add(new ArrayList<>(route));
        if (route.size() == nums.length) return;

        for (int i = start; i < end; i++) {
            route.add(nums[i]);
            findSubset(nums, result, route, i + 1, end);
            route.remove(route.size() - 1);
        }
    }
}