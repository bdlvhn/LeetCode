class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        temp = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                temp += prices[i] - prices[i-1]
            else:
                answer += temp
                temp = 0
        answer += temp
        return answer