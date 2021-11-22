class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Map<String, Boolean> map = new HashMap<>();
        return canConstruct(s, wordDict, map);
    }

    private boolean canConstruct(String target, List<String> wordDict, Map<String, Boolean> map) {
        if (map.containsKey(target)) return map.get(target);

        if (target.length() == 0) return true;

        for (String word : wordDict) {
            if (target.startsWith(word)) {
                if (canConstruct(target.substring(word.length()), wordDict, map)) {
                    map.put(target, true);
                    return true;
                }
            }
        }
        map.put(target,false);
        return false;
    }
}