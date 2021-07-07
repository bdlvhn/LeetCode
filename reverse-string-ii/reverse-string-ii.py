class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        runner = 0
        while runner < len(s) - 1:
            s[runner:runner+2*k] = s[runner:runner+k][::-1] + s[runner+k:runner+2*k]
            runner += 2*k
        return ''.join(s)