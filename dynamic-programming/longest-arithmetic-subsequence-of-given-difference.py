class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        dp[i]: len of longest subseq has diff=difference unitl i-th number
        dp[i]: (
            for j from 0->i
            max( dp[j] if nums[i]-nums[j]==diff )
        )
        """
        dp = defaultdict(int)

        for num in arr:
            num_before = dp[num - difference]
            dp[num] = num_before+1

        return max(dp.values())