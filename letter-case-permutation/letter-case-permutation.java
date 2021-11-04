class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> result = new ArrayList<>();
        doPermutation(result, new StringBuilder(), 0, s);
        return result;
    }

    private void doPermutation(List<String> result, StringBuilder temp, int index, String s) {
        if (index == s.length()) {
            result.add(temp.toString());
            return;
        }

        char c = s.charAt(index);
        if (Character.isLetter(c)) {
            temp.append(Character.toUpperCase(c));
            doPermutation(result, temp, index + 1, s);
            temp.deleteCharAt(temp.length() - 1);
            temp.append(Character.toLowerCase(c));
            doPermutation(result, temp, index + 1, s);
            temp.deleteCharAt(temp.length() - 1);
        } else {
            temp.append(c);
            doPermutation(result, temp, index + 1, s);
            temp.deleteCharAt(temp.length() - 1);
        }
    }
}