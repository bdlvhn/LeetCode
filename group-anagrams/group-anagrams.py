class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            anagrams[key].append(str)
        answer = []
        return list(anagrams.values())