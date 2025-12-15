class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        """
        dp[i]: number of smooth descent periods from index 0...i
        dp[i]: (
            if val_i == vai_prev_i-1 -> add 1 (for current i) and num of smooth descent sub_arr that ends at i
            otherwise, add 1 (for current i)
        )
        """
        n = len(prices)
        dp = [0]*n
        
        # base case
        dp[0] = 1
        prev_smooth_idx = 0

        for i in range(1, n):
            if prices[i] != prices[i-1] - 1:
                prev_smooth_idx = i

            dp[i] = dp[i-1] + 1 # add current i
            dp[i] += i - prev_smooth_idx

        return dp[n-1]