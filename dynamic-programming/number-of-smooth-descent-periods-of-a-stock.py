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

        # base case
        # can be optimized to use just a variable "ans"
        # dp = [0]*n
        ans = 1 # dp[0] = 1

        prev_smooth_idx = 0

        for i in range(1, n):
            if prices[i] != prices[i-1] - 1:
                prev_smooth_idx = i

            # add current i (itself is valid)
            ans += 1 # dp[i] = dp[i-1] + 1

            # add num of subarr that continuously decrease
            ans += i - prev_smooth_idx # dp[i] += i - prev_smooth_idx

        return ans #dp[n-1]