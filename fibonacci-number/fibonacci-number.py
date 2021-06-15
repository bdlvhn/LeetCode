class Solution:
    dp: List[int] = [-1]*(30+1)
    dp[0] = 0
    dp[1] = 1
    def fib(self, n: int) -> int:
        if n <= 1:
            return self.dp[n]
        
        if self.dp[n] == -1:
            self.dp[n] = self.fib(n-2) + self.fib(n-1)
        
        return self.dp[n]