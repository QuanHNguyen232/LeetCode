class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        dp[i]: len of longest incr subseqs until i-th number
        dp[i] = max( if nums[j] < nums[i] --> dp[j] for j from 0->i) + 1
        """
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = 0
                    if dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        
        max_length = max(dp)
        result = 0
        
        for i in range(n):
            if dp[i] == max_length:
                result += count[i]
        
        return result