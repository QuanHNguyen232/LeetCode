class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        [1,2,3], target = 4
        dp[4] = sum(
            3 + 1
            2 + (1+1 or 2)
            1 + (1+3 or 1+2+1 or etc.)
        )

        dp[i]: no. of combinations that add up to target
        dp[i] = sum(
            dp[i-num]+1
            for num in nums
        )
        """
        dp = [0] * (target+1)
        dp[0] = 1

        for curr_num in range(1, target+1):
            dp[curr_num] = sum([
                dp[curr_num-num] for num in nums if curr_num - num >= 0
            ])
            # for num in nums:
            #     if curr_num - num >= 0:
            #         dp[curr_num] += dp[curr_num-num]

        return dp[target]