class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> result = new ArrayList<>();
        ArrayList<Integer> route = new ArrayList<>();
        route.add(0);
        findPath(graph, 0, route, result);
        return result;
    }

    private void findPath(int[][] graph, int node, List<Integer> route, List<List<Integer>> result) {
        if (node == graph.length - 1) {
            ArrayList<Integer> temp = new ArrayList<>();
            temp.addAll(route);
            result.add(temp);
            return;
        }

        for (int val : graph[node]) {
            Integer next = Integer.valueOf(val);
            route.add(next);
            findPath(graph, next, route, result);
            route.remove(next);
        }
    }
}