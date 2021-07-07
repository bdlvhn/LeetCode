import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = re.compile('[a-zA-Z0-9]+')
        sentence = ''.join(p.findall(s)).lower()
        print(sentence)
        return sentence == sentence[::-1]