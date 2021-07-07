class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = ['a','e','i','o','u']
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].lower() not in vowel:
                left += 1
                continue
            if s[right].lower() not in vowel:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)