class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.length() == 0) return result;
        HashMap<Character, String> dict = new HashMap<Character, String>() {
            {
                put('2', "abc"); put('3',"def");
                put('4',"ghi"); put('5',"jkl");
                put('6',"mno"); put('7',"pqrs");
                put('8',"tuv"); put('9',"wxyz");
                }
            };
        findCombinations(digits, result, dict, 0, "");
        return result;
    }

    private void findCombinations(String digits, List<String> result,
                                  HashMap<Character, String> dict, int start, String s) {
        if (start == digits.length()) {
            result.add(s);
            return;
        }

        String temp = dict.get(digits.charAt(start));
        for (int j = 0; j < temp.length(); j++) {
            findCombinations(digits, result, dict, start + 1, s + temp.charAt(j));
        }
    }
}