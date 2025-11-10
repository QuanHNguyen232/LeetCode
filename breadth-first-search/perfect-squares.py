class Solution:
    def numSquares(self, n: int) -> int:
        """
        Unbound Knapsack
        dp[i] = min(
            dp[i-square] for each square
        )
        """
        squares = [i**2 for i in range(1, math.ceil(sqrt(n)))]
        dp = [float('inf')] * (n+1)
        for square in squares:
            dp[square] = 1

        for i in range(1, n+1):
            for square in squares:
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]