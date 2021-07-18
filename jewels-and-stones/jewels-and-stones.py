class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = collections.defaultdict(int)
        count = 0
        for jewel in jewels:
            dict[jewel] = 1

        for stone in stones:
            if dict[stone]:
                count += 1
        return count