class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());

        Arrays.sort(nums);
        for (int num : nums) {
            List<List<Integer>> newSubset = new ArrayList<>();

            for (List<Integer> elm : result) {
                newSubset.add(new ArrayList<>(elm) {{
                    add(num);
                }});
            }

            for (List<Integer> elm : newSubset) {
                if (!result.contains(elm)) result.add(elm);
            }
        }
        return result;
    }
}