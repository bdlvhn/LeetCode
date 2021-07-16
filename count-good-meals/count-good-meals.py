class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        dict = collections.defaultdict(int)

        degrees = [2 ** i for i in range(22)]

        for d in deliciousness:
            for j in range(22):
                count += dict[2 ** j - d]
            dict[d] += 1

        return count % 1000000007