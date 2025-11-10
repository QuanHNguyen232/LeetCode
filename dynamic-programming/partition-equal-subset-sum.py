class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        goal: find subset that sums to subset_sum
        dp[i]: is subset including nums[i] that sums to subset_sum (dp[subset_sum]: final result)
        Similar to https://leetcode.com/problems/coin-change-ii/
        """
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        subset_sum = total_sum // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            for i in range(1, subset_sum+1):
                if i >= num:
                    dp[i] += dp[i-num]

        return dp[subset_sum] > 0