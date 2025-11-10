class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i]: max profit at day i-th
        dp[i] = 
        """
        n = len(prices)
        dp = [0] * n
        buy = prices[0]
        dp[0] = 0
        for i in range(1, n):
            if buy <= prices[i]:
                dp[i] = prices[i] - buy

            dp[i] += dp[i-1]
            buy = prices[i]

        return dp[-1]

    def sln_1(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans