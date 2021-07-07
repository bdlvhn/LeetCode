class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = collections.Counter(re.findall('[a-z]+',paragraph.lower()))
        for b_word in banned:
            words[b_word] = 0
        print(words)
        return words.most_common(1)[0][0]