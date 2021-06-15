class Solution:
    steps = collections.defaultdict(int)
    steps[0] = 1
    steps[1] = 1

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return self.steps[n]

        if self.steps[n] > 0:
            return self.steps[n]
        self.steps[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.steps[n]