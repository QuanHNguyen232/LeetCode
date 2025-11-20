class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # return self.dp_1d(nums)
        return self.dp_2d(nums)

    def dp_1d(self, nums: List[int]) -> bool:
        """
        goal: find subset that sums to subset_sum
        Similar to https://leetcode.com/problems/coin-change-ii/
        dp[i]: is subset including nums[i] that sums to subset_sum (dp[subset_sum]: final result)
        dp[i] = OR(
            dp[i-num] for each num in [remain nums]
        )
        """
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        subset_sum = total_sum // 2
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[subset_sum]
    
    def dp_2d(self, nums: List[int]) -> bool:
        """0/1 Knapsack
        target_sum = total_sum // 2
        dp[i][j]: can sum, items [0:i] (inclusive), sum = j
        dp[i][j] = (
            if not take: dp[i-1][j]
            if take: dp[i-1][j - num] if j - num >= 0
        )
        0<= i < len(nums)
        0<= j <= sum
        """
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2
        n = len(nums)
        dp = [[False]*(target_sum+1) for _ in range(n)]
        # base case
        dp[0][0] = True

        # DP
        for i in range(1, n):
            for j in range(target_sum+1):
                not_take = dp[i-1][j]
                take = dp[i-1][j - nums[i]] if j - nums[i] >= 0 else False
                dp[i][j] = not_take or take
        return dp[n-1][target_sum]