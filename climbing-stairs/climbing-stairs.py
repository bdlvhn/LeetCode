class Solution:
    dict = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if self.dict[n]:
            return self.dict[n]
        
        self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dict[n]