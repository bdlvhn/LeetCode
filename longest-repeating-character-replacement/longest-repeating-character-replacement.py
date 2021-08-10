class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = max_count = 0
        count = collections.defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            max_count = max(max_count, count[s[i]])
            if max_length < k + max_count:
                max_length += 1
            else:
                count[s[i-max_length]] -= 1
        return max_length