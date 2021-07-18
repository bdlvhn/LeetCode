class Solution:
    def frequencySort(self, s: str) -> str:
        dict = collections.defaultdict(int)
        answer = ''
        for char in s:
            dict[char] += 1

        for char, times in sorted(dict.items(), key=lambda x: -1 * x[1]):
            answer += char * times

        return answer