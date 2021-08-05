class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = collections.defaultdict(int)
        dict_t = collections.defaultdict(int)
        
        for char_s in s:
            dict_s[char_s] += 1
        for char_t in t:
            dict_t[char_t] += 1
        
        return dict_s == dict_t