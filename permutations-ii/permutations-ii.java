class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        HashMap<Integer, Integer> dict = new HashMap<>();

        for (int num : nums) dict.put(num, dict.getOrDefault(num, 0) + 1);
        backTrack(result, dict, nums.length, new ArrayList<>());
        return result;
    }

    private void backTrack(List<List<Integer>> result, HashMap<Integer, Integer> dict, int i, ArrayList<Integer> route) {
        if (i == 0) {
            result.add(new ArrayList<>(route));
            return;
        }

        for (Integer key : dict.keySet()) {
            if (dict.get(key) > 0) {
                route.add(key);
                dict.replace(key, dict.get(key) - 1);
                backTrack(result, dict, i-1, route);
                route.remove(route.size() - 1);
                dict.replace(key, dict.get(key) + 1);
            }
        }
    }
}