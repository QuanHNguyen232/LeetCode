class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [7,1,5,3,6,4]
        
        dp[i]: max profit earn when sell on day i-th
        dp[i] = .dp[i-1] (earn yesterday)
                .prices[i] - min_buy (earn today = sell today - min_buy)
        min_buy = min(prices[:i])
        """
        n = len(prices)
        dp = [0] * n
        min_buy = prices[0]
        dp[0] = 0
        for i in range(1, n):
            dp[i] = max(
                dp[i-1],
                prices[i] - min_buy
            )
            min_buy = min(min_buy, prices[i])


        return dp[-1]
