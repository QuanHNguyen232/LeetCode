class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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