class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        left, right = 0, len(s)-1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return (s[left+1:right+1] == s[left+1:right+1][::-1]) or (s[left:right] == s[left:right][::-1])

        return True