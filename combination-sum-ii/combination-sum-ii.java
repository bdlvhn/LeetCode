class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        ArrayList<Integer> arr = new ArrayList<>();
        boolean[] visited = new boolean[candidates.length];
        doCombination2(candidates, target, arr, visited, 0, 0, result);
        return result;
    }

    private void doCombination2(int[] candidates, int target, ArrayList<Integer> arr, boolean[] visited, int start, int sum, List<List<Integer>> result) {
        if (sum == target) {
            result.add(new ArrayList<>(arr));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (sum + candidates[i] > target | visited[i] | (i > 0 && candidates[i] == candidates[i-1] && !visited[i-1])) continue;
            arr.add(candidates[i]); visited[i] = true;
            doCombination2(candidates, target, arr, visited, i,sum + candidates[i], result);
            arr.remove(arr.size() - 1); visited[i] = false;
        }
    }
}