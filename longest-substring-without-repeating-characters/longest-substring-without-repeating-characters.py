class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0

        while right < len(s):
            if s[right] in s[left:right]:
                max_len = max(max_len, right - left)
                left = left + s[left:right].index(s[right]) + 1
            right += 1

        max_len = max(max_len, right - left)
        return max_len