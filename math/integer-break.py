class Solution:
    def integerBreak(self, n: int) -> int:
        """unbound knapsack
        n = 2 --> 1+1 (cannot be 2+0 since 2 is n)
        n = 3 --> 1+2 or 2+1 or 1+1+1
        n = 4 --> 2+2 or 3+1 or 1+1+1+1

        dp[i]: max product of integers that sum up to i
        dp[i] = max(
            for each j in [1,i-1] --> dp[i]*dp[i-j]
        )
        """
        if n <= 3:
            return n - 1
        
        dp = [0]*(n+1)
        # base case
        for i in [1, 2, 3]:
            dp[i] = i

        for i in range(4, n+1):
            end = i
            # small optimize: end = (i//2)+1
            for j in range(1, end):
                dp[i] = max(dp[i], dp[j]*dp[i-j])

        return dp[n]