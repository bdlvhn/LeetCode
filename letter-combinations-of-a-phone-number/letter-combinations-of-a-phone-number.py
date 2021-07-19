class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        def dfs(s: str, arr: List) -> List:
            if not s:
                return arr
            if not arr:
                arr = dfs(s[1:], dict[s[0]])
            else:
                arr = dfs(s[1:], list(map(''.join, itertools.product(arr, dict[s[0]]))))
            return arr

        return list(dfs(digits, []))